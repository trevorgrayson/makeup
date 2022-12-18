from makeup import workflow


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


def thenthis(rows):
    return [(row[0]*10, row[1]) for row in rows]


def alsothis(features):
    """arbitrary return"""
    return features[0]


def finale(model, *args, **kwargs):
    return model(*args, **kwargs)


workflow({
    thenthis: load,
    alsothis: thenthis,
    finale: alsothis
})
