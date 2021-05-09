#!/usr/bin/env bash

set -e
set -x

flake8 tests
black tests --check
isort tests scripts --check-only
