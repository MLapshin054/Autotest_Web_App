import pytest
import yaml
import requests

with open("config.yaml") as f:
    data = yaml.safe_load(f)


@pytest.fixture()
def login():
    res1 = requests.post(data["address"] + "gateway/login",
                         data={"username": data["username"], "password": data["password"]})
    return res1.json()["token"]


@pytest.fixture()
def testtext1():
    return "New post for auto"


@pytest.fixture()
def testtext2():
    return "Some description"
