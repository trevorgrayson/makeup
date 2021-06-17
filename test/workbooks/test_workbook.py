from obviate import workflow, run


def load():
    return [
        (1, 'whiskey'),
        (2, 'foxtrot'),
        (3, 'tango')
    ]


def features(data):
    return [(row[0]*10, row[1]) for row in data]


def train(data):
    return data


workflow({
    features: load,
    train: features
})


def test_features():
    result = run(__name__, 'train')
    assert 10 == result[0][0]
