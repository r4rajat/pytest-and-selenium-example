import pytest
from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
import time


@pytest.fixture(scope="module")
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()


@pytest.mark.parametrize("url", ["https://the-internet.herokuapp.com/"])
def test_selenium(driver, url):
    driver.get(url)
    driver.maximize_window()
    assert driver.title == "The Internet"

    # Wait for 3 seconds
    time.sleep(3)

    # Test Dropdowns
    driver.find_element(By.XPATH, '//*[@id="content"]/ul/li[11]/a').click()
    time.sleep(2)
    dropdown = driver.find_element(By.ID, "dropdown")
    Select(dropdown).select_by_visible_text("Option 1")
    time.sleep(2)

    # Go Back
    driver.back()

    # Test Form Authentication
    driver.find_element(By.LINK_TEXT, "Form Authentication").click()
    time.sleep(2)
    driver.find_element(By.NAME, "username").send_keys("tomsmith")
    driver.find_element(By.NAME, "password").send_keys("SuperSecretPassword!")
    driver.find_element(By.ID, "login").click()
    time.sleep(2)

    # Go Back
    driver.back()

    # Test Checkboxes
    driver.find_element(By.LINK_TEXT, "Checkboxes").click()
    time.sleep(2)
    checkbox1 = driver.find_element(By.XPATH, '//*[@id="checkboxes"]/input[1]')
    checkbox2 = driver.find_element(By.XPATH, '//*[@id="checkboxes"]/input[2]')
    checkbox1.click()
    checkbox2.click()
    time.sleep(2)

    # Go Back
    driver.back()

    # Test Drag and Drop
    driver.find_element(By.LINK_TEXT, "Drag and Drop").click()
    time.sleep(2)
    source = driver.find_element(By.ID, "column-a")
    target = driver.find_element(By.ID, "column-b")
    webdriver.ActionChains(driver).drag_and_drop(source, target).perform()
    time.sleep(2)

    # Go Back
    driver.back()

    # Test Dynamic Content
    driver.find_element(By.LINK_TEXT, "Dynamic Content").click()
    time.sleep(2)
    driver.refresh()
    time.sleep(2)

    # Go Back
    driver.back()

    # Test Dynamic Controls
    driver.find_element(By.LINK_TEXT, "Dynamic Controls").click()
    time.sleep(2)
    driver.find_element(By.XPATH, '/html/body/div[2]/div/div[1]/form[1]/button').click()
    time.sleep(2)
    driver.find_element(By.XPATH, '/html/body/div[2]/div/div[1]/form[1]/button').click()
    time.sleep(2)
    driver.find_element(By.XPATH, '/html/body/div[2]/div/div[1]/form[2]/button').click()
    time.sleep(2)
    driver.find_element(By.XPATH, '/html/body/div[2]/div/div[1]/form[2]/button').click()
    time.sleep(2)

    # Go Back
    driver.back()

    # Test Exit Intent
    driver.find_element(By.LINK_TEXT, "Exit Intent").click()
    time.sleep(2)
    driver.find_element(By.XPATH, '/html/body/div[2]/div/div[1]/form/input').click()
    time.sleep(2)
    driver.find_element(By.XPATH, '/html/body/div[2]/div/div[1]/form/input').click()
    time.sleep(2)



