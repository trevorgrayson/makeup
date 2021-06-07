PYTHON?=python
VENV?=venv

export PYTHONPATH = .:$(VENV)

test: compile
	$(PYTHON) -m pytest $(TEST)

integ: compile
	$(PYTHON) -m pytest -o pytest.integ.ini $(TEST)

requirements.txt:
	touch requirements.txt

compile: $(VENV)
$(VENV): requirements.txt
	mkdir -p $(VENV)
	$(PYTHON) -m pip -V || curl https://bootstrap.pypa.io/get-pip.py | $(PYTHON)
	$(PYTHON) -m pip install -q -t $(VENV) -r requirements.txt
	touch $(VENV)

clean:
	find . -name "*.pyc" -delete
	rm -rf `find . -name __pycache__`
	rm -rf $(VENV)

.PHONY: test
