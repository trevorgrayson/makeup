import logging
import importlib
from makeup.deps import run, default
from inspect import isfunction, getfullargspec

# logging.basicConfig("")


def to_pascal_case(snake_str):
    comp = snake_str.split('_')
    return ''.join(x.title() for x in comp)


def get_module(model_name):
    """
    get_module
    """
    model_name = model_name.replace('/','.')

    if model_name.endswith('.py'):
        model_name = model_name[:-3]

    module_path = model_name.split('.')

    module = importlib.import_module(model_name)

    try:
        return module

    except AttributeError as err: 
        raise AttributeError("class not found in module: %s" % err.message)


def get_targets(module):
    fns = filter(lambda m: isfunction(getattr(module, m)),
                 dir(module))
    return [f for f in fns]


def target_args(fn):
    spec = getfullargspec(fn)
    return spec.args


def main(model_name, target, *args, **kwargs):
    model = get_module(model_name)
    workflow = getattr(model, 'workflow', default)
    workflow(model)

    # check here if arg list is right length, no catch.
    logging.info("Passing args: %s (%s)" % (target, " ".join(args)))
    result = run(model, target, *args, **kwargs)

    print(result)
