from selenium import Webdriver

chrome_driver_path = "C:/Users/ananthan/chrome webdriver/chromedriver.ext"
driver = Webdriver.Chrome(executable_path= chrome_driver_path)

driver.get("www.amazon.com")

print("workj")