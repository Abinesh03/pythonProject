from lib2to3.pgen2 import driver
from lib2to3.pgen2.driver import Driver

import drive as drive
from selenium import webdriver
from selenium.webdriver.common.keys import keys
import time


Account_Email = "Ananthan"
Account_Password = "Tools@1234"

chrome_drive_path = "C:/Users/ananthan/chrome webdriver/chromedriver.ext"
Driver.get("https://login.networks.nokia.com/login/login.jsp?TYPE=33554433&REALMOID=06-eecf208b-809f-44ac-ba6e-498739fae112&GUID=&SMAUTHREASON=0&METHOD=GET&SMAGENTNAME=$SM$tIhrcm%2f9I7fq5I0W8rcGNvC5EqZ3RXqS6tSkvUktYafYLMncBmmy1i3Z4oNMBbA%2f&TARGET=$SM$HTTPS%3a%2f%2flogin%2enetworks%2enokia%2ecom%2fdcpcc%2f%3fTYPE%3d33554433%26REALMOID%3d06-1eb34a53-15d7-41f4-b3ee-f27cb4cc848a%26GUID%3d%26SMAUTHREASON%3d0%26METHOD%3dGET%26SMAGENTNAME%3d$$SM$$9Nh$%2bVuR4gf0CTVy3LchGQxIWbd3BZQgZyNNwg0vJbCKgzde5UNO0xOUDULYvqiI5%26TARGET%3d$$SM$$https$%3a$%2f$%2fonline$%2enetworks$%2enokia$%2ecom$%2fnam$%2findex$%2efaces")

sign_in_button = drive.find_element_by_link_text("sing in")
sign_in_button.clicks()

time.sleep(5)

email_field = driver.find_element_by_id("username")
email_field.send_keys(Account_Email)

password_field = driver.find_element_by_id("password")
password_field.send_keys(Account_Password)
password_field.send_keys(keys.ENTER)
