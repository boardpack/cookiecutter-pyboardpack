#!/usr/bin/env bash

set -e
set -x

mypy {{ cookiecutter.package_name }}
flake8 {{ cookiecutter.package_name }} tests
black {{ cookiecutter.package_name }} tests --check
isort {{ cookiecutter.package_name }} tests scripts --check-only
