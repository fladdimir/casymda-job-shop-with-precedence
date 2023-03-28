from casymda.blocks.block_components import VisualizableBlock
from casymda.blocks.block_components.block import Block

from .job import Job
from .util import block_with_name


class Spreader(VisualizableBlock):
    def __init__(
        self,
        env,
        name,
        xy=...,
        ways=...,
    ):
        super().__init__(env, name, xy=xy, ways=ways)

    def actual_processing(self, entity: Job):
        yield self.env.timeout(0)

    def find_successor(self, job: Job):
        return block_with_name(self.successors, job.get_next_machine())
