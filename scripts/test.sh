#!/usr/bin/env bash

set -e
set -x

SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )"

bash ./scripts/lint.sh

export PYTHONPATH="$SCRIPT_DIR/.."
pytest tests --verbose
