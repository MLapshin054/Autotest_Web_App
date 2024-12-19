import requests
import yaml

with open("config.yaml") as f:
    data = yaml.safe_load(f)


def test_step01(login, testtext1):
    header = {"X-Auth-Token": login}
    res = requests.get(data["address"] + "api/posts", params={"owner": "notMe"}, headers=header)
    listres = [i["title"] for i in res.json()["data"]]

    assert testtext1 in listres


def test_step02(login):
    # Create new post
    header = {"X-Auth-Token": login}
    new_post_data = {
        "title": data["title"],
        "description": data["description"],
        "content": data["content"]
    }
    response = requests.post(data["address"] + "api/posts", json=new_post_data, headers=header)

    assert response.status_code == 200


def test_step03(login, testtext2):
    header = {"X-Auth-Token": login}
    res = requests.get(data["address"] + "api/posts", headers=header)
    listres = [i["description"] for i in res.json()["data"]]

    assert testtext2 in listres
