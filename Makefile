K ?= *

prof:
	kernprof -v -l -b -o /dev/null py.test -k "$K"
