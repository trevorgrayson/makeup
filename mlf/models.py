import sys
import inspect
import importlib


CLI = 'cli'


class MlfBase:
    
    LOAD_MODULE = None

    def execute(self, *args):
        loaded = []
        
        if args:
            # args should be read as variables, 
            # unless '--' arg is found, then all files
            is_file = False
            load_args = []

            for arg in args:
                if arg == '--':
                    is_file = True
                    continue

                if is_file:
                    load_args.append(open(arg, 'r'))
                else:
                    load_args.append(arg)
            loaded = self.load(*load_args)

        else:
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
