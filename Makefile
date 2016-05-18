pylint-src:
	python3 -m pylint src/**/*.py

pylint-tests:
	python3 -m pylint src/**/*.py

pylint: pylint-src pylint-tests

test: pylint-tests

build: pylint test
