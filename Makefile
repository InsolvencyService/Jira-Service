define green
	@tput setaf 2
	@tput bold
	@echo $1
	@tput sgr0
endef

in_venv=venv/bin/activate

.PHONY: default
default: clean venv clean_pyc flake8 tests wheel
	$(call green,"[Build successful]")

venv: venv/bin/activate
venv/bin/activate: requirements.dev.txt
	test -d venv || virtualenv venv --python=/usr/local/lib/python2.7.11/bin/python
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
