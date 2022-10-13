from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import time







def genFBaccount(firstname, lastname, email, password, mounth, day, year, gender):

    # Step 1) Open Browser
    browser = webdriver.Chrome() # OR : browser = webdriver.Chrome(executable_path="PATH_HERE")

    # Step 2) Navigate to Facebook
    browser.get("http://www.facebook.com")

    # Step 3) Accept Cookies
    browser.find_element(By.XPATH, '//*[text()="Only allow essential cookies"]').click()

    # Step 4) Click on Create new account
    time.sleep(2)
    browser.find_element(By.XPATH, '//*[text()="Create new account"]').click()

    # Complete the form
    time.sleep(3)
    browser.find_element(By.NAME, "firstname").send_keys(firstname)
    browser.find_element(By.NAME, "lastname").send_keys(lastname)
    browser.find_element(By.NAME, "reg_email__").send_keys(email)
    

    browser.find_element(By.NAME, "reg_passwd__").send_keys(password)

    MonthSel = Select(browser.find_element(By.XPATH, '//select[@title="Month"]'))
    MonthSel.select_by_visible_text(mounth)
    DaySel = Select(browser.find_element(By.XPATH, '//select[@title="Day"]'))
    DaySel.select_by_visible_text(day)
    YearSel = Select(browser.find_element(By.XPATH, '//select[@title="Year"]'))
    YearSel.select_by_visible_text(year)


    browser.find_element(By.NAME, "reg_email_confirmation__").send_keys(email)
    
    time.sleep(1)
    if gender == "Male":
        browser.find_element(By.XPATH, '//label[text()="Male"]').click()
    else :
        browser.find_element(By.XPATH, '//label[text()="Female"]').click()

    


    # Click on  Sign Up
    browser.find_element(By.XPATH, '//button[text()="Sign Up"]').click()

    time.sleep(30)

    # Continue to captcha verification




    #


