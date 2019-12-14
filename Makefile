$(shell test -f Makef.io || curl -o Makef.io makef.io/python)
include Makef.io
-include projects.Makefile

PYTHON?=python3
export PYTHONPATH = venv:.

