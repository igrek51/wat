.PHONY: venv test clean build dist

SHELL := /bin/bash

venv:
	python3 -m venv venv &&\
	. venv/bin/activate &&\
	pip install --upgrade pip &&\
	pip install -r requirements.txt -r requirements-dev.txt &&\
	python -m pip install -e .

venv-test-unit:
	python3 -m venv venv &&\
	. venv/bin/activate &&\
	pip install -r requirements.txt -r requirements-dev.txt &&\
	python -m pip install -e .

install-local:
	python -m pip install -e .

test:
	python -m coverage run --source wat -m pytest -vv --tb=short -ra --color=yes $(test)
	python -m coverage report --show-missing --skip-empty --skip-covered

clean:
	rm -rf build/
	rm -rf dist/
	rm -rf ./*.egg-info

build:
	python -m build --sdist --wheel

release: clean build
	python -m twine upload -u __token__ dist/*

mkdocs-local:
	mkdocs serve

mkdocs-push:
	mkdocs gh-deploy --force

dump-inspect:
	python wat/inspection/insta/dump.py wat/inspection/inspection.py
	@echo
	@echo "paste it to: README.md"
	@echo "paste it to: docs/index.md"
	@echo "paste it to: wat/inspection/insta/instaload.py"

example-inspect:
	python docs/example/inspection.py
