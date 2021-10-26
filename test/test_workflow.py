from makeup.deps import DEPS, target, default, run
from examples import customwf as model


class TestDeps:
    def test_target(self):
        assert DEPS[model.finale] == model.alsothis

    def test_run(self):
        assert run(model, 'alsothis') == (10, 'ollie')

    def test_default(self):
        default(model)  # TODO need to init this somewhere
        assert run(model, 'alsothis') == (10, 'ollie')
