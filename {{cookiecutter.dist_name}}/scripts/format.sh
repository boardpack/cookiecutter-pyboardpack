#!/bin/sh -e
set -x

autoflake --remove-all-unused-imports --recursive --remove-unused-variables --in-place {{ cookiecutter.package_name }} tests scripts --exclude=__init__.py
black {{ cookiecutter.package_name }} tests scripts
isort {{ cookiecutter.package_name }} tests scripts
