define green
	@tput setaf 2
	@tput bold
	@echo $1
	@tput sgr0
endef

BUILD_NUMBER ?= 0

in_venv=venv/bin/activate

.PHONY: default
default: clean clean_pyc venv clean_pyc flake8 tests wheel docker_build docker_run
	$(call green,"[Build successful]")

venv: venv/bin/activate
venv/bin/activate: requirements.dev.txt
	test -d venv || virtualenv venv
	. venv/bin/activate; pip install -r requirements.dev.txt
	$(call green,"[Making venv successful]")

.PHONY: clean
clean:
	rm -rf venv

.PHONY: clean_pyc
clean_pyc:
	find . -name "*.pyc" -delete
	$(call green,"[Cleanup loitering pyc files]")

.PHONY: flake8
flake8: venv
	. $(in_venv); flake8 --ignore F401,E402 --max-line-length=120 jira_receiver/*.py
	$(call green,"[Static analysis successful]")

.PHONY: tests
tests: venv
	. $(in_venv); . ./config_test; nosetests --nocapture -q --with-xunit --exe --cover-package=jira_receiver --with-coverage
	$(call green,"[Unit tests successful]")

.PHONY: run_jira_service
run_jira_service: venv
	. $(in_venv); . ./config_test; gunicorn jira_receiver:app

.PHONY: wheel
wheel:
	. $(in_venv); python setup.py bdist_wheel
	$(call green,"[Build of Wheel Successful]")

.PHONY: docker_build
docker_build:
	docker build -t jira-receiver:$(BUILD_NUMBER) --build-arg BUILD_NUMBER=$(BUILD_NUMBER) .
	$(call green,"[Build of Container Successful]")

.PHONY: docker_run
docker_run:
	docker-compose up
	$(call green,"[Build of Container Successful]")
