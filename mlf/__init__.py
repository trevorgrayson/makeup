from . import models
from .deps import target, default

__all__ = [models.MlfBase]


class Runner:
    def execute(self, model, *args):
        pass
