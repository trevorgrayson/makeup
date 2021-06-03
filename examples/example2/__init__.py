def load():
    """
    should always accept no arguments?
    :return:
    """
    # open("test/fixtures/module_level.tsv")
    return [
        (1, 'ollie'),
        (2, 'bobby')
    ]


def features(rows):
    return [(row[0]*10, row[1]) for row in rows]


def train(features):
    """arbitrary return"""
    return features[0]


def predict(model, *args, **kwargs):
    return model(*args, **kwargs)
