import inspect


class MlfBase:

    def execute(self):
        members = inspect.getargspec(self.run).args[1:]
        #args = map(lambda name: globals()[name], members)
        args = map(lambda name: getattr(self.LOAD_MODULE, name)(), members)
        
        loaded = self.load(*args)
        self.run(*loaded)

