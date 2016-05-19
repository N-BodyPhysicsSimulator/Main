PY=python3
files=src/**/*.py

pylint-src:
	$(PY) -m pylint $(files)

pylint: pylint-src

test: pylint-tests
	$(PY) -m doctest $(files)

build: pylint test
