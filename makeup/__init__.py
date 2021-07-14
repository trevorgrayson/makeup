from . import models
from .deps import target, default, run, workflow

__all__ = [models.MlfBase, run, workflow]


class Runner:
    def execute(self, model, *args):
        pass
