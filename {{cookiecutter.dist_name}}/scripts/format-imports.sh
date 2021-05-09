#!/bin/sh -e
set -x

# Sort imports one per line, so autoflake can remove unused imports
isort {{ cookiecutter.package_name }} tests scripts --force-single-line-imports
sh ./scripts/format.sh
