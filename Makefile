PANTS:=pants
APP_NAME:=microservices
APP_IMAGE:=microservices

SHELL=/bin/bash



.PHONY: all
all:
	$(PANTS) check ::
	$(PANTS) lint ::
	$(PANTS) fmt ::

.PHONY: tailor
tailor:
	$(PANTS) tailor ::

.PHONY: tailor-check
tailor-check:
	$(PANTS) tailor --check ::

.PHONY: fmt
fmt:
	$(PANTS) fmt ::

.PHONY: check
check:
	$(PANTS) check ::

.PHONY: lint
lint:
	$(PANTS) lint ::

.PHONY: generate-lockfiles
generate-lockfiles:
	$(PANTS) generate-lockfiles

.PHONY: generate-lockfiles-mypy
generate-lockfiles-mypy:
	$(PANTS) generate-lockfiles --resolve=mypy

.PHONY: generate-lockfiles-bandit
generate-lockfiles-bandit:
	$(PANTS) generate-lockfiles --resolve=bandit

.PHONY: generate-lockfiles-black
generate-lockfiles-black:
	$(PANTS) generate-lockfiles --resolve=black

.PHONY: generate-lockfiles-docformatter
generate-lockfiles-docformatter:
	$(PANTS) generate-lockfiles --resolve=docformatter



.PHONY: package
package:
	$(PANTS) package ::

.PHONY: update-build-files
update-build-files:
	$(PANTS) update-build-files ::

#
.PHONY: microservices-package
microservices-package:
	GIT_COMMIT='latest' $(PANTS) package src/python/$(APP_IMAGE):

.PHONY: microservices-run-binary
microservices-run-binary:
	$(PANTS) run src/python/$(APP_IMAGE):$(APP_IMAGE)

.PHONY: microservices-run-python
microservices-run-python:
	$(PANTS) run src/python/$(APP_IMAGE)/$(APP_NAME)/main.py
