import time
import yaml
from module import Site

with open("./testdata.yaml") as f:
    testdata = yaml.safe_load(f)

site = Site(testdata["address"])


class TestNegative:

    def test_step1(self, site_action, x_selector1, x_selector2, x_selector3, btn_selector, er1):
        input1 = site.find_element("xpath", x_selector1)
        input1.send_keys("test")

        input2 = site.find_element("xpath", x_selector2)
        input2.send_keys("test")

        btn = site.find_element("css", btn_selector)
        btn.click()

        time.sleep(testdata["wait"])

        err_label = site.find_element("xpath", x_selector3)
        text = err_label.text
        assert text == er1


class TestPositive:
    def test_step1(self, site_action, x_selector1, x_selector2, x_selector4, btn_selector, er2):
        input1 = site.find_element("xpath", x_selector1)
        input1.clear()
        input1.send_keys(testdata["username"])

        input2 = site.find_element("xpath", x_selector2)
        input2.clear()
        input2.send_keys(testdata["password"])

        btn = site.find_element("css", btn_selector)
        btn.click()

        time.sleep(testdata["wait"])

        user_label = site.find_element("xpath", x_selector4)
        text = user_label.text
        assert text == er2

    def test_step2(self, site_action, x_selector1, x_selector2, btn_selector, create_btn_selector, x_selector5,
                   save_btn_selector, post_title_selector, er3):
        input1 = site.find_element("xpath", x_selector1)
        input1.clear()
        input1.send_keys(testdata["username"])

        input2 = site.find_element("xpath", x_selector2)
        input2.clear()
        input2.send_keys(testdata["password"])

        btn = site.find_element("css", btn_selector)
        btn.click()

        time.sleep(testdata["wait"])

        create_btn = site.find_element("xpath", create_btn_selector)
        create_btn.click()
        input5 = site.find_element("xpath", x_selector5)

        input5.clear()
        input5.send_keys(testdata["title"])

        save_btn = site.find_element("xpath", save_btn_selector)
        save_btn.click()

        time.sleep(testdata["wait"])

        post_title = site.find_element("xpath", post_title_selector)
        text = post_title.text
        assert text == er3
