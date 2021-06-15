import logging
from urllib import parse
from urllib.request import urlopen
import pickle
import csv
from io import StringIO
# TODO: switch to urllib3
# TODO include kwargs in url params ?param1=...

OPENER = urlopen
ENCODING = 'utf-8'
SERIALIZER = pickle


def serializer(url):
    if url.endswith('tsv'):
        return csv.reader
    if url.endswith('csv'):
        return csv.reader
    return SERIALIZER


def is_url(string):
    try:
        parse.urlparse(string)
    except Exception:
        logging.debug(f"Could not parse as url: {string}")
        return False
    return True


def depickle(data):
    decoded = data.read()
    try:  # TODO reconsider
        decoded = decoded.decode(ENCODING)
    except UnicodeDecodeError:
        pass
    return SERIALIZER.loads(decoded)


def url_open(url):
    data = OPENER(url)

    if url.endswith('tsv'):
        data = StringIO(data.read().decode(ENCODING))
        return [row for row in csv.reader(data, delimiter='\t')]
    if url.endswith('csv'):
        data = StringIO(data.read().decode(ENCODING))
        return [row for row in csv.reader(data)]
    return depickle(data)


def cache_by_url(fn, url, *args, **kwargs):
    """
    args and kwargs are arguments that will be passed to fn

    """
    artifact = url + '/' + fn.__name__
    izer = serializer(url)

    try:
        result = url_open(artifact)
    except Exception:
        logging.info("CACHE MISS: %s %s" % (fn.__name__, url))
        result = fn(*args, **kwargs)

        with OPENER(artifact, 'wb') as writer:
            writer.write(izer.dumps(result))
        
    return result
