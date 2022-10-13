from selenium import webdriver
from selenium.webdriver.common.by import By
import time


def genMailCowBox(mailcowUrl, mailcowUsername, mailcowPassword, newUsername, newFullName, newPassword, delay=2):

    # Step 1) Open Browser
    browser = webdriver.Chrome() # OR : browser = webdriver.Chrome(executable_path="PATH_HERE")

    # Step 2) Navigate to MailCow url
    browser.get(mailcowUrl)

    # Enter username and password
    browser.find_element(By.NAME, "login_user").send_keys(mailcowUsername)
    browser.find_element(By.NAME, "pass_user").send_keys(mailcowPassword)


    # Click on login
    browser.find_element(By.XPATH, '//button[text()="Login"]').click()
    time.sleep(delay)

    # Click on Mailboxes
    browser.find_element(By.XPATH, '//*[@id="top"]/div[2]/ul/li[2]/a').click()

    # Click on Add Mailbox
    browser.find_element(By.XPATH, '//*[@id="tab-mailboxes"]/div/div[1]/div/button[1]').click()
    time.sleep(delay)

    # Enter username
    browser.find_element(By.NAME, "local_part").send_keys(newUsername)

    # Enter Full Name
    browser.find_element(By.NAME, "name").send_keys(newFullName)

    # Enter and Re-Enter password
    browser.find_element(By.NAME, "password").send_keys(newPassword)
    browser.find_element(By.NAME, "password2").send_keys(newPassword)


    # Click Add
    browser.find_element(By.XPATH, '//*[@id="addMailboxModal"]/div/div/div[2]/form/div[9]/div/button').click()


    time.sleep(5)
    print("ok")
