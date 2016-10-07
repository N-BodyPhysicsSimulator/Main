PY=python3.5
files=nbp/**/*.py
module=nbp

pylint-src:
	$(PY) -m pylint $(module)

pylint: pylint-src

test:
	$(PY) -m pytest $(module) --doctest-modules
	$(PY) -m pytest --capture=sys $(module) tests --doctest-modules

build: install-requirements pylint test

codecov:
	$(PY) -m pytest --capture=sys $(module) tests --doctest-modules --cov=$(module) --cov=tests
	codecov

install-requirements: install-requirements-app install-requirements-dev

install-requirements-app:
	pip install -r requirements.txt

install-requirements-dev:
	pip install -r requirements-dev.txt
