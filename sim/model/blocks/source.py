from collections import OrderedDict

from casymda.blocks.block_components import VisualizableBlock
from casymda.blocks.entity import Entity
from simpy.core import Environment
from simpy.events import AllOf, ProcessGenerator

from .job import Job

job_data: dict[str, OrderedDict[str, float]] = {
    # p1 + dependencies
    "product_1": OrderedDict([("A4", 15), ("A5", 25)]),
    "product_1_1": OrderedDict([("A1", 17), ("A2", 30)]),
    "product_1_2": OrderedDict([("A3", 14)]),
    # p2 + dependencies
    "product_2": OrderedDict([("A2", 10), ("A6", 20)]),
    "product_2_1": OrderedDict([("A1", 13)]),
    "product_2_2": OrderedDict([("A3", 15)]),
}

job_dependencies: dict[str, tuple[str]] = {
    "product_1": ("product_1_1", "product_1_2"),
    "product_2": ("product_2_1", "product_2_2"),
}


class Source(VisualizableBlock):
    def __init__(
        self,
        env: Environment,
        name: str,
        xy: tuple[int, int] = ...,
        ways: dict[str, list[tuple[int, int]]] = ...,
    ):
        super().__init__(env, name, xy=xy, ways=ways)
        env.process(self.creation_loop())

    def creation_loop(self) -> ProcessGenerator:
        # create all jobs
        jobs: dict[str, Job] = {}
        for job_id, machine_times in job_data.items():
            dependencies = job_dependencies.get(job_id, ())
            job = Job(
                self.env,
                job_id,
                machines_times=machine_times,
                dependencies=dependencies,
            )
            jobs[job_id] = job

        # let each job subscribe to the completion of the jobs it depends on
        for job in jobs.values():
            preceding_jobs_completion_events = []
            for predecessor_name in job_dependencies.get(job.name, ()):
                preceding_job = jobs[predecessor_name]
                preceding_jobs_completion_events.append(
                    preceding_job.is_completed_event
                )
            if len(preceding_jobs_completion_events) == 0:
                job.on_is_ready(None)
            else:
                env = self.env
                all_preceding_jobs_completed = AllOf(
                    env, preceding_jobs_completion_events
                )
                all_preceding_jobs_completed.callbacks.append(
                    job.is_ready_event.succeed
                )

        # start regular processing
        for job in jobs.values():
            job.block_resource_request = self.block_resource.request()
            yield job.block_resource_request
            self.env.process(self.process_entity(job))

    def actual_processing(self, entity: Entity):
        yield self.env.timeout(0)
