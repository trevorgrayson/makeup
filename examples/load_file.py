from makeup import target

load = "file:./test/fixtures/data.tsv"


def features(data):
    return data


target(features, load)
