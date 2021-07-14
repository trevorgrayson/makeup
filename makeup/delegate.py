"""
Presuming openurl style syntax on datasets,
must respond to `read()`
"""
import sys
import importlib


def get_delegate(delegate):
    if isinstance(delegate, str):
        module = sys.modules.get(delegate)
        if module:
            return module
        module = importlib.import_module(delegate)
        return module
    return delegate


def load(delegate, dataset=None):
    """
    Prefer returning the dataset, if available
    :param self: delegate
    :param dataset: can be URL or df
    :return:
    """
    if isinstance(dataset, str) and ':' not in dataset:
        return open(dataset)
    elif dataset is not None:
        # possibly better condition:
        # getattr(dataset, 'read')
        return dataset

    delegate = get_delegate(delegate)
    if getattr(delegate, 'load'):
        return delegate.load()


def features(delegate, dataset=None):
    delegate = get_delegate(delegate)
    data = load(delegate, dataset)
    return delegate.features(data)
