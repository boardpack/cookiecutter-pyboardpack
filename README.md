# cookiecutter-pyboardpack

<a href="https://github.com/boardpack/cookiecutter-pyboardpack/actions?query=workflow%3ATest">
  <img src="https://github.com/boardpack/cookiecutter-pyboardpack/workflows/Test/badge.svg" alt="Test">
</a>
<a href="https://github.com/cookiecutter/cookiecutter">
  <img src="https://img.shields.io/badge/cookiecutter-template-D4AA00.svg?style=flat-square&logo=cookiecutter" alt="Cookiecutter template badge">
</a>
<a href="https://opensource.org/licenses/MIT">
  <img src="https://img.shields.io/badge/License-MIT-blue.svg" alt="License: MIT">
</a>

Cookiecutter template for a Python 3.6+ package for Boardpack projects.

## Features

- [X] Documentation with [`MkDocs`](https://github.com/mkdocs/mkdocs) with [`Material theme`](https://github.com/squidfunk/mkdocs-material)
- [X] Formatting with [`isort`](https://github.com/timothycrosley/isort), [`flake8`](https://github.com/PyCQA/flake8) and [`black`](https://github.com/psf/black)
- [X] Testing setup with [`pytest`](https://github.com/pytest-dev/pytest)
- [X] [`Tox`](https://github.com/tox-dev/tox) testing: setup to easily test for Python 3.6, 3.7, 3.8, 3.9
- [X] Comes with [pre-commit](https://pre-commit.com/) hook config for black, isort, flake8, mypy
- [X] Static typing with [`mypy`](http://mypy-lang.org/)
- [X] Dependencies kept up to date by [`dependabot`](https://docs.github.com/en/code-security/supply-chain-security/keeping-your-dependencies-updated-automatically)
- [X] Automatic packaging with [`flit`](https://github.com/takluyver/flit)
- [X] Ready-to-use [GitHub Actions](https://help.github.com/en/actions/automating-your-workflow-with-github-actions) pipelines:
    - [X] Netlify Preview documentation deployment
    - [X] First PR greeting
    - [X] Testing
    - [X] Package publishing

## Quickstart checklist

* Enable the GitHub repository in Dependabot
* Enable the GitHub repository in [Codecov](https://codecov.io/gh)
* Add the next environment variables:
    * CODECOV_TOKEN
    * FLIT_USERNAME and FLIT_PASSWORD (username/password from your [pypi.org](https://pypi.org/) account)
    * NETLIFY_AUTH_TOKEN and NETLIFY_SITE_ID (you can find [here](https://github.com/marketplace/actions/netlify-actions#required-inputs-and-env) how to get those tokens)
* Replace default images in the docs and README.md

## Acknowledgments

When creating this template, the following repositories were used (special thanks to [Sebastián Ramírez](https://github.com/tiangolo) and his [FastAPI](https://github.com/tiangolo/fastapi) project,  some scripts and documentation structure and parts were used from there):

- https://github.com/tiangolo/fastapi
- https://github.com/audreyfeldroy/cookiecutter-pypackage
- https://github.com/sourcery-ai/python-best-practices-cookiecutter
- https://github.com/frankie567/cookiecutter-hipster-pypackage
- https://github.com/browniebroke/cookiecutter-pypackage

## License

This project is licensed under the terms of the MIT license.
