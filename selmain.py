from selenium import webdriver
from selenium.webdriver.common.by import By
chromeDriverPath= "C:\chromedriver\chromedriver.exe"

driver = webdriver.Chrome(executable_path=chromeDriverPath)

driver.get("https://www.collegepravesh.com/engineering-colleges/iet-lucknow/#courses")

price= driver.find_element(By.XPATH, '//*[@id="courses-41"]/div[2]/div/ul')
print(price)
