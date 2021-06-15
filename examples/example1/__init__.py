def load():
    """
    should always accept no arguments?
    :return:
    """
    return [
        (1, 'ollie'),
        (2, 'bobby'),
        (3, 'alice')
    ]


def features(rows, **kw):
    return [(row[0]*10, row[1]) for row in rows]


def train(features, **kw):
    """arbitrary return"""
    return features[0]


def predict(model, *args, **kwargs):
    return model(*args, **kwargs)
