from BaseApp import BasePage
from selenium.webdriver.common.by import By
import logging, yaml, requests

with open("./testdata.yaml") as f:
    testdata = yaml.safe_load(f)


class TestSearchLocators:
    ids = dict()
    with open("./locators.yaml") as f:
        locators = yaml.safe_load(f)
        for locator in locators["xpath"].keys():
            ids[locator] = (By.XPATH, locators["xpath"][locator])
        for locator in locators["css"].keys():
            ids[locator] = (By.CSS_SELECTOR, locators["css"][locator])


class OperationsHelper(BasePage):

    def enter_text_into_field(self, locator, word, description=None):
        if description:
            element_name = description
        else:
            element_name = locator
        logging.debug(f"Send {word} to element {element_name}")
        field = self.find_element(locator)
        if not field:
            logging.error(f"Element {locator} not found")
            return False
        try:
            field.clear()
            field.send_keys(word)
        except:
            logging.exception(f"Exception while operation with {locator}")
            return False
        return True

    def click_button(self, locator, description=None):
        if description:
            element_name = description
        else:
            element_name = locator
        button = self.find_element(locator)
        if not button:
            return False
        try:
            button.click()
        except:
            logging.exception("Exception with click")
            return False
        logging.debug(f"Clicked {element_name} button")
        return True

    def get_text_from_element(self, locator, description=None):
        if description:
            element_name = description
        else:
            element_name = locator
        field = self.find_element(locator, time=5)
        if not field:
            return None
        try:
            text = field.text
        except:
            logging.exception(f"Exception while get text from {element_name}")
            return None
        logging.debug(f"We find text {text} in field {element_name}")
        return text

    def get_text_from_value(self, locator, description=None):
        if description:
            value = description
        else:
            value = locator
        field = self.find_element(locator, time=5)
        if not field:
            return None
        try:
            text = field.get_attribute("value")
        except:
            logging.exception(f"Exception while get text from {value}")
            return None
        logging.debug(f"We find text {text} in value {value}")
        return text

    # ENTER TEXT
    def enter_login(self, word):
        self.enter_text_into_field(TestSearchLocators.ids["LOCATOR_LOGIN_FIELD"], word, description="login form")

    def enter_pass(self, word):
        self.enter_text_into_field(TestSearchLocators.ids["LOCATOR_PASS_FIELD"], word, description="password form")

    def enter_title(self, word):
        self.enter_text_into_field(TestSearchLocators.ids["LOCATOR_TITLE_INPUT"], word, description="post title")

    def enter_description(self, word):
        self.enter_text_into_field(TestSearchLocators.ids["LOCATOR_DESCRIPTION_INPUT"], word,
                                   description="post description")

    def enter_content(self, word):
        self.enter_text_into_field(TestSearchLocators.ids["LOCATOR_CONTENT_INPUT"], word, description="post content")

    def enter_contact_name(self, word):
        self.enter_text_into_field(TestSearchLocators.ids["LOCATOR_CONTACT_NAME"], word, description="contact name")

    def enter_contact_email(self, word):
        self.enter_text_into_field(TestSearchLocators.ids["LOCATOR_CONTACT_EMAIL"], word, description="contact email")

    def enter_contact_content(self, word):
        self.enter_text_into_field(TestSearchLocators.ids["LOCATOR_CONTACT_CONTENT"], word,
                                   description="contact content")

    # CLICK
    def click_login_button(self):
        self.click_button(TestSearchLocators.ids["LOCATOR_LOGIN_BTN"], description="login")

    def click_new_post_btn(self):
        self.click_button(TestSearchLocators.ids["LOCATOR_CREATE_POST_BTN"], description="new post")

    def click_save_btn(self):
        self.click_button(TestSearchLocators.ids["LOCATOR_SAVE_POST_BTN"], description="save post")

    def click_contact_link(self):
        self.click_button(TestSearchLocators.ids["LOCATOR_CONTACT_BTN"], description="contact")

    def click_contact_save_btn(self):
        self.click_button(TestSearchLocators.ids["LOCATOR_CONTACT_SAVE_BTN"], description="send contact")

    # GET TEXT
    def get_error_text(self):
        return self.get_text_from_element(TestSearchLocators.ids["LOCATOR_ERROR_FIELD"], description="error label")

    def get_user_text(self):
        return self.get_text_from_element(TestSearchLocators.ids["LOCATOR_HELLO_FIELD"], description="username")

    def get_res_text(self):
        return self.get_text_from_element(TestSearchLocators.ids["LOCATOR_POST_TITLE"], description="result")

    def get_contact_title(self):
        return self.get_text_from_element(TestSearchLocators.ids["LOCATOR_CONTACT_TITLE"], description="contact title")

    def get_contact_name(self):
        return self.get_text_from_value(TestSearchLocators.ids["LOCATOR_CONTACT_NAME"], description="contact name")

    def get_contact_email(self):
        return self.get_text_from_value(TestSearchLocators.ids["LOCATOR_CONTACT_EMAIL"], description="contact email")

    def get_contact_content(self):
        return self.get_text_from_value(TestSearchLocators.ids["LOCATOR_CONTACT_CONTENT"],
                                        description="contact content")

    def get_contact_alert(self):
        logging.info("Get Contact alert text")
        text = self.get_alert_text()
        logging.info(text)
        return text


class ApiOperations():

    def __init__(self, base_url, auth_token):
        self.base_url = base_url
        self.auth_token = auth_token
        self.headers = {"X-Auth-Token": self.auth_token}

    def get_posts(self, params=None):
        logging.debug("Try get posts")
        try:
            response = requests.get(f"{self.base_url}api/posts", headers=self.headers, params=params)
            response.raise_for_status()
            return response.json().get("data", [])
        except:
            logging.error(f"Don't get posts {response.text}")
            return None

    def create_post(self, title, description, content):
        new_post_data = {
            "title": title,
            "description": description,
            "content": content
        }
        try:
            response = requests.post(f"{self.base_url}api/posts", json=new_post_data, headers=self.headers)
            response.raise_for_status()  # Вызывает исключение для статусов 4xx и 5xx
            return response.json()
        except:
            logging.error(f"Don't create post {response.text}")
            return None

    def assert_text_in_posts(self, text, field='title', params=None):
        try:
            posts = self.get_posts(params)
            if posts is None:
                return False
            listres = [i[field] for i in posts]
            #print(f'Text for assertion is -> {listres[0]}') # ---> выдает в консоль заголовок для сравнения в тест API1
            return text in listres
        except:
            logging.exception("Exception while assertion")
            return False

    def assert_text_in_post_descriptions(self, text):
        return self.assert_text_in_posts(text, field='description')
