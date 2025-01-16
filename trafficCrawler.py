from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import time
import json
import os

chrome_options = Options()
chrome_options.add_argument("--headless")  # 后台运行
chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument("--no-sandbox")

driver = webdriver.Chrome(options=chrome_options)

# 从环境变量中获取 GitHub 用户名和密码
github_username = os.getenv("MY_USERNAME")  # 从环境变量加载
github_password = os.getenv("MY_PASSWORD")  # 从环境变量加载

try:
    login_url = "https://github.com/login"
    driver.get(login_url)

    username_input = driver.find_element(By.ID, "login_field")
    password_input = driver.find_element(By.ID, "password")

    username_input.send_keys(github_username)
    password_input.send_keys(github_password)

    password_input.send_keys(Keys.RETURN)
    time.sleep(5)

    traffic_url = "https://github.com/FDU2023DS/FDU2023DS.github.io/graphs/traffic"
    driver.get(traffic_url)
    time.sleep(5)

    views_element = driver.find_element(By.CLASS_NAME, "js-traffic-total.visits")
    uniques_element = driver.find_element(By.CLASS_NAME, "js-traffic-uniques.uniques")

    views = views_element.text
    uniques = uniques_element.text

    traffic_data = {
        "Views": views,
        "Unique Visitors": uniques
    }

    with open("traffic_data.json", "w") as json_file:
        json.dump(traffic_data, json_file, indent=4)

    # print(f"Views: {views}")
    # print(f"Unique Visitors: {uniques}")

finally:
    driver.quit()