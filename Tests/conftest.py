import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.opera import OperaDriverManager
from webdriver_manager.core.utils import ChromeType
from webdriver_manager.microsoft import IEDriverManager


@pytest.fixture(params=["chrome"], scope='class')  # - add more browsers in params
def init_driver(request):
    global web_driver
    if request.param == "chrome":
        web_driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    if request.param == "firefox":
        web_driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
    if request.param == "edge":
        web_driver = webdriver.Chrome(service=Service(ChromeDriverManager(chrome_type=ChromeType.MSEDGE).install()))
    if request.param == "opera":
        web_driver = webdriver.Opera(executable_path=OperaDriverManager().install())
    if request.param == "chromium":
        web_driver = webdriver.Chrome(service=Service(ChromeDriverManager(chrome_type=ChromeType.CHROMIUM).install()))
    if request.param == "brave":
        web_driver = webdriver.Chrome(service=Service(ChromeDriverManager(chrome_type=ChromeType.BRAVE).install()))
    if request.param == "internet explorer":
        web_driver = webdriver.Ie(service=Service(IEDriverManager().install()))

    request.cls.driver = web_driver
    web_driver.implicitly_wait(10)
    yield
    web_driver.quit()
