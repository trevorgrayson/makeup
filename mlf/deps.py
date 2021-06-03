#
# Put functions into DEPS as key, put deps in values
#
DEPS = {}


def target(fn, requires, **kwargs):
    DEPS[fn] = requires


def run(model, verb, *args, **kwargs):
    """
    take model and verb,
    run required preconditions,
    and then execute verb.
    """
    if isinstance(verb, str):
        verb = getattr(model, verb)
    if verb is None:
        raise Exception(f"{model} does not have method {verb}")
    exec_stack = []

    if verb in DEPS:
        return verb(run(model, DEPS[verb], *args, **kwargs),
                    *args, **kwargs)  # reconsider
    return verb(*args, **kwargs)



def default(model):
    """default target dependencies which can be used.

    predict -> train
    train -> features
    features -> load
    """
    target(model.features, requires=model.load)
    target(model.train, requires=model.features)
    target(model.predict, requires=model.train)
