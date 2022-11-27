#!/usr/bin/env bash

set -e
set -x

SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )"

cookiecutter . --no-input --config-file ./tests/default_context.yml

cd boardpack_project

python -m venv venv && source venv/bin/activate

pip install flit

flit install
