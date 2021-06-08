#
# Put functions into DEPS as key, put deps in values
#
from mlf.url_cache import cache_by_url


DEPS = {}


def target(fn, requires, **kwargs):
    DEPS[fn] = requires


def run(model, verb, *args, **kwargs):
    """
    take model and verb,
    run required preconditions,
    and then execute verb.
    """
    RUNNER = run
    url = kwargs.get('url_cache')
    if url:
        RUNNER = cache_by_url

    if isinstance(verb, str):
        verb = getattr(model, verb)
    if verb is None:
        raise Exception(f"{model} does not have method {verb}")
    exec_stack = []

    # TODO this doesn't cache for last method.
    #  use run(verb, *args, **kwargs)
    if verb in DEPS:
        result = RUNNER(model, DEPS[verb], *args, **kwargs)
        if not hasattr(result, '__iter__'):
            result = result,
        return verb(*result, *args, **kwargs)  # reconsider
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
