K ?= *

prof:
	kernprof -v -l -b -o /dev/null py.test -k "$K"

clean: clean-pyc

clean-pyc:
	find . -name '*.pyc' -exec rm -f {} +
	find . -name '*.pyo' -exec rm -f {} +
	find . -name '*~' -exec rm -f {} +
	-find ${VIRTUAL_ENV} -name '*.pyc' -delete
