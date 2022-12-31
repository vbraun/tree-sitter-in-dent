
.PHONY: lint
lint: \
    lint-isort \
    lint-mypy \
    lint-flake8


.PHONY: lint-mypy
lint-mypy:
	$(TOOL)/mypy --config-file config/mypy.ini -p dent
	$(TOOL)/mypy --config-file config/mypy.ini -p test


.PHONY: lint-flake8
lint-flake8:
	$(TOOL)/flake8 --statistics --config config/flake8-test dent test


.PHONY: lint-isort
lint-isort:
	$(TOOL)/isort --settings config/isort.cfg dent test


