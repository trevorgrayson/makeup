import sys
import importlib
import logging


def to_pascal_case(snake_str):
    comp = snake_str.split('_')
    return ''.join(x.title() for x in comp)


def get_class(model_name):
    module_path = model_name.split('.')
    klass = to_pascal_case(module_path[-1])

    module = importlib.import_module(model_name)

    try:
        return getattr(module, klass)

    except AttributeError as err:
        raise AttributeError("class not found in module")


def main(model_name, *args, **kwargs):
    Klass = get_class(model_name)


    try:
        model = Klass()
        model.execute(*args)

    except TypeError as err:
        print("TypeError: Do you have the right " +
              "number of arguments for `%s`? >> %s" %
              (model_name, err))
