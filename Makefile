PY=python3
files=nbp/**/*.py
module=nbp

pylint-src:
	$(PY) -m pylint $(module)

pylint: pylint-src

test:
	py.test --doctest-modules

build: pylint test

pull-request: pylint
