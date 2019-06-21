import inspect
import importlib


class MlfBase:
    
    LOAD_MODULE = None

    def execute(self):
        members = inspect.getargspec(self.run).args[1:]
        #args = map(lambda name: globals()[name], members)
        args = map(lambda name: getattr(self.load_module(), name)(), members)
        
        loaded = self.cached(*args)

        if loaded is None:
            loaded = self.load(*args)

        self.run(*loaded)


    def cached(self, *args):
        """ if this function returns a non-None value, load will be skipped."""
        return None

        
    def load_module(self):
        if self.LOAD_MODULE is None:
            sibling = ".".join(self.__class__.__module__.split('.')[:-1]) + '.data'
            data = importlib.import_module(sibling)

            return data

        return self.LOAD_MODULE
        

    def load(self, *args, **kwargs):
        """ load your data set. if not instantiated, original arguments will be passed. """
        return args
