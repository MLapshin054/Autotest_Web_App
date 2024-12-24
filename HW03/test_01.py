import time
import yaml
from testpage import OperationsHelper
import logging

with open("./testdata.yaml") as f:
    testdata = yaml.safe_load(f)

name = testdata["username"]
password = testdata["password"]
contact_us_name = testdata["contact_us_name"]
contact_us_email = testdata["contact_us_email"]
contact_us_content = testdata["contact_us_content"]


class TestNegative:

    def test_step1(self, browser):
        logging.info("Negative test 1 Start")
        testpage = OperationsHelper(browser)
        testpage.go_to_site()
        testpage.enter_login("test")
        testpage.enter_pass("test")
        testpage.click_login_button()
        assert testpage.get_error_text() == "401"


class TestPositive:

    def test_step1(self, browser):
        logging.info("Positive test 1 Start")
        testpage = OperationsHelper(browser)
        testpage.enter_login(name)
        testpage.enter_pass(password)
        testpage.click_login_button()
        assert testpage.get_user_text() == f'Hello, {name}'

    def test_step2(self, browser):
        logging.info("Positive test 2 Start")
        testpage = OperationsHelper(browser)
        testpage.click_new_post_btn()
        testpage.enter_title(testdata["post_title"])
        testpage.enter_description(testdata["post_description"])
        testpage.enter_content(testdata["post_content"])
        testpage.click_save_btn()
        time.sleep(testdata["wait"])
        assert testpage.get_res_text() == testdata["post_title"]

    def test_step3(self, browser):
        logging.info("Positive test 3 Start")
        testpage = OperationsHelper(browser)
        testpage.click_contact_link()
        time.sleep(testdata["wait"])
        assert testpage.get_contact_title() == "Contact us!"

    def test_step4(self, browser):
        logging.info("Positive test 4 Start")
        testpage = OperationsHelper(browser)
        testpage.enter_contact_name(contact_us_name)
        assert testpage.get_contact_name() == contact_us_name

    def test_step5(self, browser):
        logging.info("Positive test 5 Start")
        testpage = OperationsHelper(browser)
        testpage.enter_contact_email(contact_us_email)
        assert testpage.get_contact_email() == contact_us_email

    def test_step6(self, browser):
        logging.info("Positive test 6 Start")
        testpage = OperationsHelper(browser)
        testpage.enter_contact_content(contact_us_content)
        assert testpage.get_contact_content() == contact_us_content

    def test_step7(self, browser):
        logging.info("Positive test 7 Start")
        testpage = OperationsHelper(browser)
        testpage.click_contact_save_btn()
        time.sleep(testdata["wait"])
        assert "Form successfully submitted" in testpage.get_contact_alert()
