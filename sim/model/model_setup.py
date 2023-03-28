from simpy.core import Environment

from .model import Model


def setup_model(env: Environment) -> Model:
    return Model(env)
