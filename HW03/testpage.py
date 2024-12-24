from BaseApp import BasePage
from selenium.webdriver.common.by import By
import logging


class TestSearchLocators:
    LOCATOR_LOGIN_FIELD = (By.XPATH, """//*[@id="login"]/div[1]/label/input""")
    LOCATOR_PASS_FIELD = (By.XPATH, """//*[@id="login"]/div[2]/label/input""")
    LOCATOR_ERROR_FIELD = (By.XPATH, """//*[@id="app"]/main/div/div/div[2]/h2""")
    LOCATOR_LOGIN_BTN = (By.CSS_SELECTOR, """button""")
    LOCATOR_HELLO_FIELD = (By.XPATH, """//*[@id="app"]/main/nav/ul/li[3]/a""")
    LOCATOR_CREATE_POST_BTN = (By.XPATH, '''//*[@id="create-btn"]''')
    LOCATOR_TITLE_INPUT = (By.XPATH, """//*[@id="create-item"]/div/div/div[1]/div/label/input""")
    LOCATOR_DESCRIPTION_INPUT = (By.XPATH, """//*[@id="create-item"]/div/div/div[2]/div/label/span/textarea""")
    LOCATOR_CONTENT_INPUT = (By.XPATH, """//*[@id="create-item"]/div/div/div[3]/div/label/span/textarea""")
    LOCATOR_SAVE_POST_BTN = (By.XPATH, """//*[@id="create-item"]/div/div/div[7]/div/button/span""")
    LOCATOR_POST_TITLE = (By.XPATH, """//*[@id="app"]/main/div/div[1]/h1""")
    LOCATOR_CONTACT_BTN = (By.XPATH, """//*[@id="app"]/main/nav/ul/li[2]/a""")
    LOCATOR_CONTACT_TITLE = (By.XPATH, """//*[@id="app"]/main/div/div/h1""")
    LOCATOR_CONTACT_NAME = (By.XPATH, """//*[@id="contact"]/div[1]/label/input""")
    LOCATOR_CONTACT_EMAIL = (By.XPATH, """//*[@id="contact"]/div[2]/label/input""")
    LOCATOR_CONTACT_CONTENT = (By.XPATH, """//*[@id="contact"]/div[3]/label/span/textarea""")
    # LOCATOR_CONTACT_SAVE_BTN = (By.XPATH, """//*[@id="contact"]/div[4]/button"""
    LOCATOR_CONTACT_SAVE_BTN = (By.CSS_SELECTOR, """button""")


class OperationsHelper(BasePage):
    def enter_login(self, word):
        logging.info(f"Send {word} in element {TestSearchLocators.LOCATOR_LOGIN_FIELD[1]}")
        login_field = self.find_element(TestSearchLocators.LOCATOR_LOGIN_FIELD)
        login_field.clear()
        login_field.send_keys(word)

    def enter_pass(self, word):
        logging.info(f"Send {word} in element {TestSearchLocators.LOCATOR_PASS_FIELD[1]}")
        login_field = self.find_element(TestSearchLocators.LOCATOR_PASS_FIELD)
        login_field.clear()
        login_field.send_keys(word)

    def click_login_button(self):
        logging.info("Click login button")
        self.find_element(TestSearchLocators.LOCATOR_LOGIN_BTN).click()

    def get_error_text(self):
        error_field = self.find_element(TestSearchLocators.LOCATOR_ERROR_FIELD, time=5)
        text = error_field.text
        logging.info(f"We find text {text} in error field{TestSearchLocators.LOCATOR_ERROR_FIELD[1]}")
        return text

    def get_user_text(self):
        user_field = self.find_element(TestSearchLocators.LOCATOR_HELLO_FIELD, time=5)
        text = user_field.text
        logging.info(f"We find text {text} in field {TestSearchLocators.LOCATOR_HELLO_FIELD[1]}")
        return text

    def click_new_post_btn(self):
        logging.info("Click new post button")
        self.find_element(TestSearchLocators.LOCATOR_CREATE_POST_BTN).click()

    def enter_title(self, word):
        logging.info(f"Send {word} to title field {TestSearchLocators.LOCATOR_TITLE_INPUT[1]}")
        login_field = self.find_element(TestSearchLocators.LOCATOR_TITLE_INPUT)
        login_field.clear()
        login_field.send_keys(word)

    def enter_description(self, word):
        logging.info(f"Send {word} to description field {TestSearchLocators.LOCATOR_DESCRIPTION_INPUT[1]}")
        login_field = self.find_element(TestSearchLocators.LOCATOR_DESCRIPTION_INPUT)
        login_field.clear()
        login_field.send_keys(word)

    def enter_content(self, word):
        logging.info(f"Send {word} to content field {TestSearchLocators.LOCATOR_CONTENT_INPUT[1]}")
        login_field = self.find_element(TestSearchLocators.LOCATOR_CONTENT_INPUT)
        login_field.clear()
        login_field.send_keys(word)

    def click_save_btn(self):
        logging.info("Click save button")
        self.find_element(TestSearchLocators.LOCATOR_SAVE_POST_BTN).click()

    def get_res_text(self):
        res_title = self.find_element(TestSearchLocators.LOCATOR_POST_TITLE, time=5)
        text = res_title.text
        logging.info(f"We find text {text} in title {TestSearchLocators.LOCATOR_POST_TITLE[1]}")
        return text

    def click_contact_link(self):
        logging.info("Click Contact link")
        self.find_element(TestSearchLocators.LOCATOR_CONTACT_BTN).click()

    def get_contact_title(self):
        title = self.find_element(TestSearchLocators.LOCATOR_CONTACT_TITLE, time=5)
        text = title.text
        logging.info(f"We find text {text} in title {TestSearchLocators.LOCATOR_CONTACT_TITLE[1]}")
        return text

    def enter_contact_name(self, word):
        logging.info(f"Send {word} to name field {TestSearchLocators.LOCATOR_CONTACT_NAME[1]}")
        name = self.find_element(TestSearchLocators.LOCATOR_CONTACT_NAME)
        name.clear()
        name.send_keys(word)

    def get_contact_name(self):
        name = self.find_element(TestSearchLocators.LOCATOR_CONTACT_NAME)
        text = name.get_attribute("value")
        logging.info(f"We find text {text} in name field {TestSearchLocators.LOCATOR_CONTACT_NAME[1]}")
        return text

    def enter_contact_email(self, word):
        logging.info(f"Send {word} to email field {TestSearchLocators.LOCATOR_CONTACT_EMAIL[1]}")
        email = self.find_element(TestSearchLocators.LOCATOR_CONTACT_EMAIL)
        email.clear()
        email.send_keys(word)

    def get_contact_email(self):
        email = self.find_element(TestSearchLocators.LOCATOR_CONTACT_EMAIL)
        text = email.get_attribute("value")
        logging.info(f"We find text {text} in email field {TestSearchLocators.LOCATOR_CONTACT_EMAIL[1]}")
        return text

    def enter_contact_content(self, word):
        logging.info(f"Send {word} to content field {TestSearchLocators.LOCATOR_CONTACT_CONTENT[1]}")
        content = self.find_element(TestSearchLocators.LOCATOR_CONTACT_CONTENT)
        content.clear()
        content.send_keys(word)

    def get_contact_content(self):
        content = self.find_element(TestSearchLocators.LOCATOR_CONTACT_CONTENT)
        text = content.get_attribute("value")
        logging.info(f"We find text {text} in content field {TestSearchLocators.LOCATOR_CONTACT_CONTENT[1]}")
        return text

    def click_contact_save_btn(self):
        logging.info("Click Contact Us button")
        self.find_element(TestSearchLocators.LOCATOR_CONTACT_SAVE_BTN).click()

    def switch_contact_alert(self):
        alert = self.driver.switch_to.alert
        text = alert.text
        logging.info(f"We find text {text} in alert")
        return text
