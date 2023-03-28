from typing import Callable

from casymda.blocks.block_components import VisualizableBlock
from simpy import Interrupt

from .job import Job


class Buffer(VisualizableBlock):
    def __init__(
        self,
        env,
        name,
        xy=None,
        ways=None,
    ):
        super().__init__(env, name, xy=xy, ways=ways)

    def actual_processing(self, job: Job):
        # just release every job as soon as it is ready
        # tbd: alternatively let a dedicated scheduler release specific jobs at certain times
        if job.is_ready:
            yield self.env.timeout(0)
        else:
            # wake up on is_ready
            job.add_on_is_ready_callback(lambda ev: job.current_process.interrupt())
            # wait
            try:
                yield self.env.timeout(float("inf"))
            except Interrupt:
                pass  # job is_ready callback executed
