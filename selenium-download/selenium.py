[9:38 AM] Ballerstein, Justin D. (SAIC)
def upload(driver, filename, location):
    driver.get(location)
    time.sleep(10)
    driver.find_element(By.ID, 'upload-button').click()
    file_uri = FILE_FOLDER + filename
    driver.find_element(By.CSS_SELECTOR, "input.upload-file-table__file-input[type='file']").send_keys(file_uri)
    driver.find_element(By.CSS_SELECTOR, "awsui-button.upload-configuration__submit").click()
    time.sleep(120)
[9:39 AM] Hagan, Douglas J. (SAIC)
you are faster than chat gpt 
[9:40 AM] Ballerstein, Justin D. (SAIC)
import threading
import keyboard, mouse
import time
import getpass
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
 
ENV = "dev" # test, dev
 
def thread_function(password):
    keyboard.press("tab")
    time.sleep(1)
    keyboard.press("tab")
    time.sleep(1)
    keyboard.press("tab")
    time.sleep(1)
    keyboard.press("enter")
    time.sleep(5)
    keyboard.write(password)
    keyboard.press("enter")
 
def choseRole(driver):
    match ENV:
            case "pte":
                driver.find_element(By.ID, 'arn:aws-us-gov:iam::227763086662:role/adfs-project-ped-pte').click()
            case "dev":
                driver.find_element(By.ID, 'arn:aws-us-gov:iam::412819066487:role/adfs-project-ped-dev').click()
            case "test":
                driver.find_element(By.ID, 'arn:aws-us-gov:iam::227763086662:role/adfs-project-ped-test').click()
            case _:
                driver.find_element(By.ID, 'arn:aws-us-gov:iam::227763086662:role/adfs-project-ped-pte').click()
 
def login(driver):
    #password = getpass.getpass("Enter pin: ")
    sender_id = '133052274      '
    aws_log_on_url = "https://prod.adfs.federation.va.gov/adfs/ls/idpinitiatedsignon.aspx"
    driver.get(aws_log_on_url)
    driver.maximize_window()
    time.sleep(20)
    driver.find_element(By.CSS_SELECTOR, 'label[for="idp_OtherRpRadioButton"').click()
    time.sleep(2)
    driver.find_element(By.ID, 'idp_RelyingPartyDropDownList').click()
    time.sleep(2)
    driver.find_element(By.CSS_SELECTOR, 'option[value="3d682b83-c219-e911-80f5-00155d61e014"]').click()
    time.sleep(2)
    driver.find_element(By.ID, 'idp_SignInButton').click()
    time.sleep(2)
    try:
        choseRole(driver)
    except NoSuchElementException:
        #driver.find_element(By.ID, 'CertificateAuthentication').click()
        #x = threading.Thread(target=thread_function(password))
        #x.start()
        time.sleep(10)
        choseRole(driver)
    time.sleep(2)
    driver.find_element(By.ID, 'signin_button').click()
    time.sleep(10)