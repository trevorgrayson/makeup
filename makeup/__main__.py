#!/user/bin/env python

import sys
from argparse import ArgumentParser
from makeup.bootstrap import main

parser = ArgumentParser(description="Run your ML models.")
parser.add_argument("model_name", type=str,
                    help="module with targets to run.")
parser.add_argument("target", type=str,
                    help="verb to run, a function name in model")
# parser.add_argument(type="*nargs", dest="args",
#                     help="arguments to be passed to starting function")
# kwargs overflow goes to load method
parser.add_argument("--load", type=str, dest='load', required=False,
                    help="alternate data to load")
args = parser.parse_args()

kwargs = {}

if args.load:
    kwargs['load'] = args.load

main(args.model_name, args.target, **kwargs)

