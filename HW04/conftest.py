import pytest
import yaml
import time
import logging
import requests
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from mail import send_email_report

with open("./testdata.yaml") as f:
    testdata = yaml.safe_load(f)
    browser = testdata["browser"]


@pytest.fixture(scope="session")
def browser():
    if browser == "firefox":
        service = Service(executable_path=GeckoDriverManager().install())
        options = webdriver.FirefoxOptions()
        driver = webdriver.Firefox(service=service, options=options)
    else:
        service = Service(executable_path=ChromeDriverManager().install())
        options = webdriver.ChromeOptions()
        #options.add_argument('--headless')
        driver = webdriver.Chrome(service=service, options=options)
    yield driver
    driver.quit()


@pytest.fixture(scope="session", autouse=True)
def send_report_after_tests(request):
    def finalizer():
        reportname = testdata["reportname"]
        fromaddr = testdata["fromaddr"]
        toaddr = testdata["toaddr"]
        mypass = testdata["mypass"]

        logging.info(f"Creating report {reportname}...")
        time.sleep(testdata["wait"])

        try:
            logging.info(f"Attempt to send report {reportname}...")
            send_email_report(reportname, fromaddr, toaddr, mypass)
            logging.info("Report sent")
        except:
            logging.error(f"Error sending report")

    request.addfinalizer(finalizer)


@pytest.fixture()
def login():
    logging.debug("Authorisation and get token")
    try:
        login = requests.post(testdata["address"] + "gateway/login",
                              data={"username": testdata["username"], "password": testdata["password"]})
        token = login.json()["token"]
        return token
    except:
        logging.exception("Exception while authorisation")


@pytest.fixture()
def testtext1():
    return "testtitle"  # Значение постоянно меняется. Перед запуском - проверить выдачу,
    # запустив тест отдельно.


@pytest.fixture()
def testtext2():
    return "Some description - API"
