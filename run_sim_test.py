from sim.model.model_setup import setup_model
from simpy.core import Environment


def test_run_sim():
    env = Environment()
    model = setup_model(env)
    env.run()
    assert model.sink.overall_count_in == 6
    assert model.sink.time_of_last_entry == 87


if __name__ == "__main__":
    test_run_sim()
