from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import pytest
import time

@pytest.fixture
def setUp():
    global username,gender,branch,address,pincode,mobile,emailid,password,confirmpassword,driver
    username = input("Enter username :")
    gender = input("Enter the gender :")
    branch = input("Enter the branch :")
    address = input("Enter the address :")
    pincode = input("Enter the pincode :")
    mobile = input("Enter the mobile :")
    emailid = input("Enter emailid :")
    password = input("Enter the password :")
    confirmpassword = input("Enter confirmpassword :")
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.maximize_window()
    yield
    time.sleep(5)
    driver.close()
def test_user(setUp):
    driver.get("https://iprimedtraining.herokuapp.com/userdata.php")
    driver.find_element_by_name("name").send_keys(username)
    time.sleep(1)
    driver.find_element_by_xpath("/html/body/div/div/div[2]/form/table/tbody/tr[2]/td[2]/input[1]").click()
    time.sleep(1)
    driver.find_element_by_name("branch").send_keys(branch)
    time.sleep(1)
    driver.find_element_by_name("Address").send_keys(address)
    time.sleep(1)
    driver.find_element_by_name("Pincode").send_keys(pincode)
    time.sleep(1)
    driver.find_element_by_name("Mobile").send_keys(mobile)
    time.sleep(1)
    driver.find_element_by_name("Email").send_keys(emailid)
    time.sleep(1)
    driver.find_element_by_name("pass").send_keys(password)
    time.sleep(1)
    driver.find_element_by_name("cnfpass").send_keys(confirmpassword)
    time.sleep(1)
    driver.find_element_by_name("subbtn").click()
    time.sleep(5)
