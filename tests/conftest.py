import pytest
import yaml


@pytest.fixture
def base_context():
    with open("./tests/default_context.yml") as fp:
        data = yaml.load(fp)

    return data["default_context"]
