.PHONY: venv test clean build dist

SHELL := bash

venv:
	uv venv venv &&\
	. venv/bin/activate &&\
	uv pip install -r requirements-dev.txt -e .

venv-test-unit:
	uv venv venv &&\
	. venv/bin/activate &&\
	uv pip install -r requirements-dev.txt -e .

install-local:
	uv pip install -e .

test:
	python -m coverage run --source wat -m pytest -vv --tb=short -ra --color=yes $(test)
	python -m coverage report --show-missing --skip-empty --skip-covered

clean:
	rm -rf build/ dist/ ./*.egg-info

build:
	python -m build --sdist --wheel

release: clean build
	python -m twine upload -u __token__ dist/*

mkdocs-local:
	mkdocs serve

mkdocs-push:
	mkdocs gh-deploy --force

# Generate Insta-Load snippet and update it in the docs
regenerate-insta-load:
	python utils/insta/regenerate.py

example-inspect:
	python utils/example/example_inspection.py

mkdocs-index:
	python utils/mkdocs_gen.py generate-index

regenerate: regenerate-insta-load mkdocs-index
