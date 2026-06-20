from selenium import webdriver
from selenium.webdriver.common.by import By

# crete variable  for lunch driver

driver = webdriver.Edge()
driver.get("https://www.google.com")

# recovery the search bar
cookies = driver.find_element(By.ID, "W0wltc")
cookies.click()

search_bar = driver.find_element(By.NAME , "q")
search_bar.send_keys("esiea")
search_bar.submit()
search_bar.click()
confirm_search_bar = driver.find_element(By.CLASS_NAME, "btnK")

