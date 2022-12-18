from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)

driver.get("http://orteil.dashnet.org/experiments/cookie/")


cookie= driver.find_element(By.ID,'cookie')
timeout = time.time() + 10
two_mins = time.time() + 60 * 2

while True:
    cookie.click()

    if time.time() > timeout:
        # get current money
        money = driver.find_element(By.ID, "money").text
        #converting string to int
        if "," in money:
            current_money = int(money.replace(",", ""))
        else:
            current_money = int(money)

        # buy tool
        store = driver.find_elements(By.CSS_SELECTOR, "#store b")
        for upgrade in store[::-1]:
            upgrade_text = upgrade.text
            print(upgrade_text)
            if upgrade_text != "":
                detail = upgrade_text.split("-")
                product = detail[0].strip()
                cost = detail[-1].strip()
                if "," in cost:
                    cost = cost.replace(",", "")
                cost_int = int(cost)
                if current_money >= cost_int:
                    #using f string to specify product name
                    driver.find_element(By.ID, f"buy{product}").click()
                    break
                else:
                    continue

        timeout = time.time() + 10
    #Stopping and printing result after 2 mins
    if time.time() > two_mins:
        cookie_per = driver.find_element(By.ID, "cps").text.split(":")
        print("Score = ", cookie_per[-1].strip())
        break





   