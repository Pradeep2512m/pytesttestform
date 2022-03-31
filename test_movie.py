from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import pytest
import time

@pytest.fixture
def setUp():
    global moviename,yof,dirname,distributor,producer,language,driver
    moviename =input("Enter the movie name")
    yof = input("Enter the release year")
    dirname = input("Enter the director name")
    distributor = input("Enter the distributor")
    producer = input("Enter the producing company")
    language = input("Enter the language")
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.maximize_window()
    yield
    driver.close()
    time.sleep(5)

def test_moviedata(setUp):
    driver.get("https://iprimedtraining.herokuapp.com/movie.php")
    driver.find_element_by_name("mname").send_keys(moviename)
    time.sleep(1)
    driver.find_element_by_name("myear").send_keys(yof)
    time.sleep(1)
    driver.find_element_by_name("mdirector").send_keys(dirname)
    time.sleep(1)
    driver.find_element_by_name("mdist").send_keys(distributor)
    time.sleep(1)
    driver.find_element_by_name("mproducer").send_keys(producer)
    time.sleep(1)
    driver.find_element_by_name("mlang").send_keys(language)
    time.sleep(1)
    driver.find_element_by_name("subbtn").click()
    time.sleep(2)
