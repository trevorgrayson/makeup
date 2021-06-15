#
# Put functions into DEPS as key, put deps in values
#
import logging
from makeup.url_cache import cache_by_url, is_url, url_open

logging.basicConfig(level=logging.INFO)

DEPS = {}


def target(fn, requires, **kwargs):
    DEPS[fn] = requires


def workflow(*dicts):
    for d in dicts:
        DEPS.update(d)


def run(model, verb, *args, **kwargs):
    """
    take model and verb,
    run required preconditions,
    and then execute verb.
    """
    if isinstance(model, str):
        model = __import__(model)
    RUNNER = run
    url = kwargs.get('url_cache')
    if url:
        RUNNER = cache_by_url

    if isinstance(verb, str):
        try:
            verb = getattr(model, verb)
        except AttributeError:
            pass
        if is_url(verb):
            return url_open(verb)

    if verb is None:  # BUG shouldn't be required if kwarg is passed
        raise Exception(f"{model} does not have method {verb}")

    # TODO this doesn't cache for last method.
    #  use run(verb, *args, **kwargs)
    arg_types = list(map(type, args))
    if verb in DEPS:
        dep = DEPS[verb]
        if callable(dep) and dep.__name__ in kwargs:
            result = url_open(kwargs[dep.__name__])
        else:
            result = RUNNER(model, dep, *args, **kwargs)
        if type(result) != tuple:  # tuples get splatted.
            result = result,
        logging.info(f"Running {verb.__name__}({','.join(arg_types)})")
        return verb(*result, *args, **kwargs)  # reconsider
    logging.info(f"Running {verb.__name__}({','.join(arg_types)})")
    return verb(*args, **kwargs)


def default(model):
    """default target dependencies which can be used.

    predict -> train
    train -> features
    features -> load
    """
    if hasattr(model, 'features'):
        target(model.features, requires=model.load)
    if hasattr(model, 'train'):
        target(model.train, requires=model.features)
    if hasattr(model, 'predict'):
        target(model.predict, requires=model.train)
