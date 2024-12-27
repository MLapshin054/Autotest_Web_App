import logging
import yaml
from testpage import ApiOperations

with open("./testdata.yaml") as f:
    testdata = yaml.safe_load(f)

class TestApi:

    def test_step1(self, login, testtext1):
        logging.info("API test 1 Start")
        api_operations = ApiOperations(testdata["address"], login)
        assert api_operations.assert_text_in_posts(testtext1, field='title', params={"owner": "notMe"})


    def test_step2(self, login):
        logging.info("API test 2 Start")
        api_operations = ApiOperations(testdata["address"], login)
        response = api_operations.create_post(testdata["title_api"], testdata["description_api"],
                                              testdata["content_api"])
        assert response is not None


    def test_step3(self, login, testtext2):
        logging.info("API test 3 Start")
        api_operations = ApiOperations(testdata["address"], login)
        assert api_operations.assert_text_in_post_descriptions(testtext2)
