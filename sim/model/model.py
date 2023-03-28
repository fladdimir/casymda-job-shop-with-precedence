from sim.model.blocks.blocks import Source, Buffer, Spreader, Machine, Check, Sink


class Model:
    """generated model"""

    def __init__(self, env):
        self.env = env

        #!resources+components

        self.source = Source(
            self.env,
            "source",
            xy=(24, 243),
            ways={"unfinished_jobs": [(42, 243), (114, 243)]},
        )

        self.sink = Sink(self.env, "sink", xy=(884, 243), ways={})

        self.unfinished_jobs = Buffer(
            self.env,
            "unfinished_jobs",
            xy=(164, 243),
            ways={"spreader": [(214, 243), (269, 243)]},
        )

        self.A1 = Machine(
            self.env,
            "A1",
            xy=(474, 43),
            ways={"is_finished": [(524, 43), (674, 43), (674, 243), (759, 243)]},
        )

        self.A2 = Machine(
            self.env,
            "A2",
            xy=(474, 143),
            ways={"is_finished": [(524, 143), (674, 143), (674, 243), (759, 243)]},
        )

        self.A3 = Machine(
            self.env,
            "A3",
            xy=(474, 243),
            ways={"is_finished": [(524, 243), (759, 243)]},
        )

        self.A4 = Machine(
            self.env,
            "A4",
            xy=(474, 343),
            ways={"is_finished": [(524, 343), (674, 343), (674, 243), (759, 243)]},
        )

        self.A5 = Machine(
            self.env,
            "A5",
            xy=(474, 443),
            ways={"is_finished": [(524, 443), (674, 443), (674, 243), (759, 243)]},
        )

        self.A6 = Machine(
            self.env,
            "A6",
            xy=(474, 543),
            ways={"is_finished": [(524, 543), (674, 543), (674, 243), (759, 243)]},
        )

        self.spreader = Spreader(
            self.env,
            "spreader",
            xy=(294, 243),
            ways={
                "A1": [(294, 218), (294, 43), (424, 43)],
                "A2": [(294, 218), (294, 143), (424, 143)],
                "A3": [(319, 243), (424, 243)],
                "A4": [(294, 268), (294, 343), (424, 343)],
                "A5": [(294, 268), (294, 443), (424, 443)],
                "A6": [(294, 268), (294, 543), (424, 543)],
            },
        )

        self.is_finished = Check(
            self.env,
            "is_finished",
            xy=(784, 243),
            ways={
                "sink": [(809, 243), (866, 243)],
                "unfinished_jobs": [(784, 268), (784, 633), (164, 633), (164, 283)],
            },
        )

        #!model

        self.model_components = {
            "source": self.source,
            "sink": self.sink,
            "unfinished_jobs": self.unfinished_jobs,
            "A1": self.A1,
            "A2": self.A2,
            "A3": self.A3,
            "A4": self.A4,
            "A5": self.A5,
            "A6": self.A6,
            "spreader": self.spreader,
            "is_finished": self.is_finished,
        }

        self.model_graph_names = {
            "source": ["unfinished_jobs"],
            "sink": [],
            "unfinished_jobs": ["spreader"],
            "A1": ["is_finished"],
            "A2": ["is_finished"],
            "A3": ["is_finished"],
            "A4": ["is_finished"],
            "A5": ["is_finished"],
            "A6": ["is_finished"],
            "spreader": ["A1", "A2", "A3", "A4", "A5", "A6"],
            "is_finished": ["sink", "unfinished_jobs"],
        }
        # translate model_graph_names into corresponding objects
        self.model_graph = {
            self.model_components[name]: [
                self.model_components[nameSucc]
                for nameSucc in self.model_graph_names[name]
            ]
            for name in self.model_graph_names
        }

        for component in self.model_graph:
            component.successors = self.model_graph[component]
