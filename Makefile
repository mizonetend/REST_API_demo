# > make help
#
# The following commands can be used.
#
# clean:	cleans the project
# env:  	Source venv and environment files for testing
# init:  	sets up environment and installs requirements
# run:  	Executes the logic
# example 	Present usefull information about the usage
# test:  	Run unit_test


VENV_PATH='finder/bin'
ENVIRONMENT_VARIABLE_FILE='.env'
MAKEFILE_LIST='Makefile'

define find.functions
	@fgrep -h "##" $(MAKEFILE_LIST) | fgrep -v fgrep | sed -e 's/\\$$//' | sed -e 's/##//'
endef

help:
	@echo 'The following commands can be used.'
	@echo ''
	$(call find.functions)
	@echo ''
	@echo 'First run "make init"'


init: ##Sets up environment and installs requirements
init: env
	$(VENV_PATH)/pip list
	$(VENV_PATH)/pip install -r requirements.txt
	@echo 'init compleated'

	
env: ##Create venv for the project
env:
	python3 -m venv finder
	$(VENV_PATH)/python -m pip install --upgrade pip
	

test: ##Runs the unit tests
test:
	$(VENV_PATH)/python src/tests.py

run: ##Runs the server
run:
	$(VENV_PATH)/python finder.py

example: ##Show usefull usage information
example:
	$(VENV_PATH)/python finder.py --example

clean: ##Cleans the projcet - removes the python virtual environment
clean:
	@rm -rf finder
	@echo 'Succesfully cleaned.'
