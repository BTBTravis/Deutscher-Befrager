# Deutscher Befrager
![Build Status Badge](https://img.shields.io/gitlab/pipeline/BTBTravis/deutscher-befrager.svg)

[![Coverage Status](https://coveralls.io/repos/gitlab/BTBTravis/deutscher-befrager/badge.svg?branch=HEAD)](https://coveralls.io/gitlab/BTBTravis/deutscher-befrager?branch=HEAD)

## Purpose

I'm in the process of learning german but I don't work in german so I made this as a way to practice
while I'm on the command line. 

## Usage

Ask questions: `$ befrager ask "Wo wohnen Sie?"` 

Answer questions: `$ befrager answer`

# Dev

## Useful links

* click docs: https://click.palletsprojects.com/en/7.x/quickstart/
* yaml docs: https://pyyaml.org/wiki/PyYAMLDocumentation
* yaml lang docs: https://yaml.org/
* yaml loader info: https://github.com/yaml/pyyaml/wiki/PyYAML-yaml.load(input)-Deprecation
* unittest: https://docs.python.org/2/library/unittest.html
* guide to unittest: https://realpython.com/python-testing/
* packaging docs: https://packaging.python.org/tutorials/packaging-projects/

## Local dev

1. clone the repo
1. cd into the folder
1. create a python env for the project and install deps with `pipenv install`
1. run commands with `pipenv run python -m interviewer.core ask "Wie heißt du?"`
1. run unit tests with `pipenv run python -m unittest discover ./interviewer/ -v`
1. run test coverage with `pipenv run coverage run --source=./interviewer -m unittest discover ./interviewer`
1. view coverage report with `pipenv run coverage report` also possilbe to create html report see
   docs [here](https://coverage.readthedocs.io/en/v4.5.x/)

## Deployment

Currently the module is deployed locally to PyPi with the following steps:

1. Before commiting remember to export requirements.txt and commit it: `$ pipenv run pip freeze > requirements.txt`
1. Start by tagging version: `$ git tag -a v0.0.2 -m 'version 0.0.2: Init PyPi capable package'`
1. clean from previous deploys: `rm -r dist`
1. build project: `python3 setup.py sdist bdist_wheel`
1. install built version locally to test: `pip3 install ./dist/deutscher-befrager-0.0.1.tar.gz`
1. push built files to PyPi: `python3 -m twine upload --repository-url https://test.pypi.org/legacy/ dist/*`
