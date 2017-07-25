.PHONY: prof clean clean-pyc unprint print install test cov htmlcov ci

clean: clean-pyc clean-test

clean-test:
	rm -rf htmlcov

clean-pyc:
	find . -name '*.pyc' -exec rm -f {} +
	find . -name '*.pyo' -exec rm -f {} +
	find . -name '*~' -exec rm -f {} +
	-find ${VIRTUAL_ENV} -name '*.pyc' -delete

FIND=find leet -type f -name *.py

unprint:
	$(FIND) -exec sed -i '' -E "s/(print.*)/# \1/g" {} \;

print:
	$(FIND) -exec sed -i '' -E "s/# (print.*)/\1/g" {} \;

install:
	pip install -r requirements.txt

lint:
	flake8

test .coverage:
	pytest --cov-report= --cov=leet --cov-fail-under=100 leet

cov: .coverage
	@coverage report --skip-covered

htmlcov: .coverage
	@coverage html --skip-covered
	@echo "open htmlcov/index.html"

ci junit.xml: clean lint
	$(MAKE) test PYTEST_ADDOPTS=--junit-xml=junit.xml htmlcov
