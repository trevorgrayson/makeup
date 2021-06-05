import urllib3
import logging
import pickle
# TODO: switch to urllib3
# TODO include kwargs in url params ?param1=...

OPENER = open
ENCODING = 'utf-8'


def cache_by_url(fn, url, *args, **kwargs):
    """
    args and kwargs are arguments that will be passed to fn

    """
    artifact = url + '/' + fn.__name__

    try:
        data = OPENER(artifact)
        result = pickle.loads(data.read().decode(ENCODING))
    except Exception:
        logging.info("CACHE MISS: %s %s" % (fn.__name__, url))
        result = fn(*args, **kwargs)

        with OPENER(artifact, 'wb') as writer:
            writer.write(pickle.dumps(result))
        
    return result
