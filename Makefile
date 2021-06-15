$(shell test -f Makef.io || curl -o Makef.io makef.io/python)
include Makef.io
-include projects.Makefile

PYTHON?=python3
export PYTHONPATH = venv:.

package: compile
	rm -rf dist
	$(PYTHON) setup.py sdist

publish: package
	@$(PYTHON) -m twine upload --verbose dist/* || echo "ERROR: pushing to pypi. Already uploaded?"
	# git push --tags
