from . import models
from .deps import target, default, run

__all__ = [models.MlfBase, run]


class Runner:
    def execute(self, model, *args):
        pass
