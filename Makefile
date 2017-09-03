.PHONY: prof clean clean-pyc unprint print install test cov htmlcov ci

clean: clean-pyc clean-test

clean-test:
	rm -rf htmlcov
	rm -rf .benchmarks

clean-pyc:
	find . -name '__pycache__' -exec rm -rf {} +
	find . -name '*.pyc' -exec rm -f {} +
	find . -name '*.pyo' -exec rm -f {} +
	find . -name '*~' -exec rm -f {} +

FIND=find leet -type f -name *.py

unprint:
	$(FIND) -exec sed -i '' -E "s/(print.*)/# \1/g" {} \;

print:
	$(FIND) -exec sed -i '' -E "s/# (print.*)/\1/g" {} \;

install:
	pip install -r requirements.txt
	pip install -e .

lint:
	flake8

test .coverage: clean
	pytest --cov-report= --cov=leet --cov-fail-under=100 --benchmark-skip

benchmark:
	pytest --benchmark-only

cov: .coverage
	@coverage report --skip-covered

htmlcov: .coverage
	@coverage html --skip-covered
	@echo "open htmlcov/index.html"

ci junit.xml: clean lint
	$(MAKE) test PYTEST_ADDOPTS=--junit-xml=junit.xml htmlcov
