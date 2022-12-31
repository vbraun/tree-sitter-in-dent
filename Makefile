export REPO_ROOT:=$(shell git rev-parse --show-toplevel)
export TOOL:=$(REPO_ROOT)/tools/bin


.PHONY: all
all: shell


.PHONY: shell
shell:
	./tools/bin/ipython


include Makefile.d/install.mk
include Makefile.d/languages.mk
include Makefile.d/lint.mk
include Makefile.d/test.mk




