#!make

# Clean pyc
.PHONY: clean-pyc
clean-pyc:
	find . -name "*.pyc" -exec rm -rf {} +

# Run lint
.PHONY: lint
lint:
	flake8 diffpriv_laplace tests

# Execute lint and tests
.PHONY: test
test: lint
	./.env tox

# Setup dependencies
.PHONY: setup
setup:
	pip install -r requirements.txt

# Build the docs
.PHONY: docs 
docs:
	-rm -r docs/
	sphinx-build docs_src/ docs/ -b html
	touch docs/.nojekyll

# Clean the /dist directory for a new publish
.PHONY: package-clean
package-clean:
	@rm -rf dist/*

# Build a new package into the /dist directory
.PHONY: package-build
package-build:
	python setup.py sdist

# Test new package before publish
.PHONY: package-check
package-check:
	twine check dist/*

# Publish the new /dist package to Pypi
.PHONY: package-publish
package-publish:
	twine upload dist/*
