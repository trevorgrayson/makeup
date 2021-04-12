import importlib


def to_pascal_case(snake_str):
    comp = snake_str.split('_')
    return ''.join(x.title() for x in comp)


def get_class(model_name):
    model_name = model_name.replace('/','.')

    if model_name.endswith('.py'):
        model_name = model_name[:-3]

    module_path = model_name.split('.')
    klass = to_pascal_case(module_path[-1])

    module = importlib.import_module(model_name)

    try:
        return getattr(module, klass)

    except AttributeError as err: 
        raise AttributeError("class not found in module: %s" % err.message)


def main(model_name, *args, **kwargs):
    Klass = get_class(model_name)

    try:
        model = Klass()

        # check here if arg list is right length, no catch.
        print("Passing args: %s" % " ".join(args))
        model.execute(*args)

    except TypeError as err: # TODO need to back off this error, too greedy
        print("TypeError: Do you have the right " +
              "number of arguments for `%s`? >> %s" %
              (model_name, err))
