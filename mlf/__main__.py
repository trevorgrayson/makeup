#!/user/bin/env python

import sys
from argparse import ArgumentParser
from mlf.bootstrap import main

parser = ArgumentParser(description="Run your ML models.")
parser.add_argument("model_name", type=str,
                    help="module with targets to run.")
parser.parse_args()

main(*sys.argv[1:])

