from casymda.blocks.block_components import VisualizableBlock
from casymda.blocks.block_components.block import Block

from .job import Job
from .util import block_with_name


class Check(VisualizableBlock):
    def __init__(
        self,
        env,
        name: str,
        xy=...,
        ways=...,
    ):
        super().__init__(env, name, xy=xy, ways=ways)

    def actual_processing(self, job: Job):
        yield self.env.timeout(0)

    def find_successor(self, job: Job) -> Block:
        job_is_done = not job.has_next_machine()
        successor_name = "sink" if job_is_done else "unfinished_jobs"
        return block_with_name(self.successors, successor_name)
