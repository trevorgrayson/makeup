import importlib
from mlf.deps import run, default


def to_pascal_case(snake_str):
    comp = snake_str.split('_')
    return ''.join(x.title() for x in comp)


def get_module(model_name, target):
    """
    get_module
    """
    model_name = model_name.replace('/','.')

    if model_name.endswith('.py'):
        model_name = model_name[:-3]

    module_path = model_name.split('.')
    # klass = to_pascal_case(module_path[-1])

    module = importlib.import_module(model_name)

    try:
        return module

    except AttributeError as err: 
        raise AttributeError("class not found in module: %s" % err.message)


def main(model_name, target, *args, **kwargs):
    model = get_module(model_name, target)

    workflow = getattr(model, 'workflow')
    if workflow:
        workflow(model)
    else:
        default(model)

    # check here if arg list is right length, no catch.
    print("Passing args: %s (%s)" % (target, " ".join(args)))
    result = run(model, target, *args)

    print(result)
