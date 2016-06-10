PY=python3
files=nbp/**/*.py
module=nbp

pylint-src:
	$(PY) -m pylint $(module)

pylint: pylint-src

test:
	$(PY) -m pytest $(module) --doctest-modules

build: pylint test

codecov:
	$(PY) -m pytest --cov=$(module)
	codecov
