#!/usr/bin/env bash

set -e
set -x

bash ./scripts/lint.sh
pytest --cov={{ cookiecutter.package_name }} --cov=tests --cov-report=term-missing --cov-report=xml tests ${@}
