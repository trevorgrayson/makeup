from makeup.deps import DEPS, target, default, run
from examples import example1 as model


class TestDeps:
    def test_target(self):
        target(model.train, requires=model.features)
        assert DEPS[model.train] == model.features

    def test_run(self):
        target(model.train, requires=model.features)
        target(model.features, requires=model.load)
        assert run(model, 'train') == (10, 'ollie')

    def test_default(self):
        default(model)  # TODO need to init this somewhere
        assert run(model, 'train') == (10, 'ollie')
