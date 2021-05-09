<p align="center">
  <a href="{{ cookiecutter.docs_url }}/"><img src="{{ cookiecutter.docs_url }}//img/logo-margin/logo-teal.png" alt="{{ cookiecutter.project_name }}"></a>
</p>
<p align="center">
    <em>{{ cookiecutter.project_short_description }}</em>
</p>
<p align="center">
    <a href="{{ cookiecutter.repository_url }}/actions?query=workflow%3ATest" target="_blank">
        <img src="{{ cookiecutter.repository_url }}/workflows/Test/badge.svg" alt="Test">
    </a>
    <a href="https://codecov.io/gh/{{ cookiecutter.github_organization }}/{{ cookiecutter.dist_name }}" target="_blank">
        <img src="https://img.shields.io/codecov/c/github/{{ cookiecutter.github_organization }}/{{ cookiecutter.dist_name }}?color=%2334D058" alt="Coverage">
    </a>
    <a href="https://pypi.org/project/{{ cookiecutter.dist_name }}" target="_blank">
        <img src="https://img.shields.io/pypi/v/{{ cookiecutter.dist_name }}?color=%2334D058&label=pypi%20package" alt="Package version">
    </a>
    <a href="https://github.com/psf/black"><img alt="Code style: black" src="https://camo.githubusercontent.com/d91ed7ac7abbd5a6102cbe988dd8e9ac21bde0a73d97be7603b891ad08ce3479/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f636f64652532307374796c652d626c61636b2d3030303030302e737667" data-canonical-src="https://img.shields.io/badge/code%20style-black-000000.svg" style="max-width:100%;"></a>
    <a href="https://pycqa.github.io/isort/" rel="nofollow"><img src="https://camo.githubusercontent.com/fe4a658dd745f746410f961ae45d44355db1cc0e4c09c7877d265c1380248943/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f253230696d706f7274732d69736f72742d2532333136373462313f7374796c653d666c6174266c6162656c436f6c6f723d656638333336" alt="Imports: isort" data-canonical-src="https://img.shields.io/badge/%20imports-isort-%231674b1?style=flat&amp;labelColor=ef8336" style="max-width:100%;"></a>
</p>

---

**Documentation**: <a href="{{ cookiecutter.docs_url }}" target="_blank">{{ cookiecutter.docs_url }}</a>

**Source Code**: <a href="{{ cookiecutter.repository_url }}" target="_blank">{{ cookiecutter.repository_url }}</a>

---

## Requirements

Python 3.6+

## Installation

<div class="termy">

```console
$ pip install {{ cookiecutter.dist_name }}

---> 100%
```

</div>

## Acknowledgments

Special thanks to [Sebastián Ramírez](https://github.com/tiangolo) and his [FastAPI](https://github.com/tiangolo/fastapi) project,  some scripts and documentation structure and parts were used from there.

## License

This project is licensed under the terms of the {{ cookiecutter.open_source_license }}.
