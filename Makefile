PY=python3
files=nbp/**/*.py

pylint-src:
	$(PY) -m pylint $(files)

pylint: pylint-src

test:
	py.test --doctest-modules

build: pylint test
