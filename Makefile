PROJECT_NAME := $(shell basename $(CURDIR))
VIRTUAL_ENVIRONMENT := $(CURDIR)/.venv
LOCAL_PYTHON := $(VIRTUAL_ENVIRONMENT)/bin/python3

define HELP
Manage $(PROJECT_NAME). Usage:

make run        - Run $(PROJECT_NAME) locally.
make install    - Create local virtualenv & install dependencies.
make deploy     - Set up project & run locally.
make update     - Update dependencies via Poetry and output resulting `requirements.txt`.
make format     - Run Python code formatter & sort dependencies.
make lint       - Check code formatting with flake8.
make clean      - Remove extraneous compiled files, caches, logs, etc.

endef
export HELP


.PHONY: run install deploy update format lint clean help


all help:
	@echo "$$HELP"


env: $(VIRTUAL_ENVIRONMENT)


$(VIRTUAL_ENVIRONMENT):
	if [ -d $(VIRTUAL_ENVIRONMENT) ]; then \
		@echo "Creating Python virtual environment..." && \
		python3 -m venv $(VIRTUAL_ENVIRONMENT) && \
	fi


.PHONY: run
run: env
	$(LOCAL_PYTHON) -m wsgi

.PHONY: install
install:
	if [ ! -d "./.venv" ]; then python3 -m venv $(VIRTUAL_ENVIRONMENT); fi
	$(shell . $(VIRTUAL_ENVIRONMENT)/bin/activate)
	$(LOCAL_PYTHON) -m pip install --upgrade pip setuptools wheel
	$(LOCAL_PYTHON) -m pip install -r requirements.txt

.PHONY: deploy
deploy: clean install run


.PHONY: update
update: env
	$(LOCAL_PYTHON) -m pip install poetry
	$(LOCAL_PYTHON) -m poetry update
	$(LOCAL_PYTHON) -m poetry export --format=requirements.txt --output=requirements.txt


.PHONY: format
format: env
	$(LOCAL_PYTHON) -m pip install black
	$(LOCAL_PYTHON) -m black .


.PHONY: lint
lint: env
	$(LOCAL_PYTHON) -m pip install flake8
	$(LOCAL_PYTHON) -m flake8 .


.PHONY: clean
clean:
	@echo "Cleaning up..."
	find . -type f -name "*.pyc" -delete
	rm -rf .pytest_cache .coverage .pytest_cache coverage.xml htmlcov


.PHONY: help
help:
	@echo "$$HELP"
