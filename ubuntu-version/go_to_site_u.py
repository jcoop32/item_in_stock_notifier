from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options

from send_text_u import send_message_one, send_message
from refresh_page import countdown

import time

import datetime

# Get the current date and time
now = datetime.datetime.now()

# Format the date and time
formatted_date = now.strftime("%Y-%m-%d")
formatted_time = now.strftime("%H:%M:%S")

service = Service(
    log_output="geckodriver.log",
    executable_path="/usr/local/bin/geckodriver",
)
options = Options()
options.add_argument("--headless")
# options.binary_location = "/opt/firefox/firefox"
driver = webdriver.Firefox(options=options, service=service)
# driver = webdriver.Firefox()

limit = 1000


def go_to_site(url):
    driver.get(url)
    print(f"On {url}")
    send_message_one(
        "2242458826",
        "att",
        f"Current time: {formatted_date}, {formatted_time}\nProgram Started, On {url}",
    )
    time.sleep(2)
    add_to_cart_btn = driver.find_element(by=By.ID, value="product-addtocart-button")
    btn_inner_text = add_to_cart_btn.get_attribute("innerText")
    if btn_inner_text.strip() == "<span>Out Of Stock</span>":
        print("Says with span")
    elif btn_inner_text.strip() == "Out Of Stock":
        print("Says without span")
    else:
        print("Neither options")
        print(btn_inner_text)
        print(len(btn_inner_text.strip()))
    print("STARTING REFRESH PHASE...")
    # for x in range(0, limit):
    #     countdown(int(60))
    #     if btn_inner_text != "OUT OF STOCK":
    #         time.sleep(1)
    #         # send_message(
    #         #     "2242458826", "8473854005", "att", f"Item back in stock go to \n{url}"
    #         # )
    #         send_message_one(
    #             "2242458826",
    #             "att",
    #             f"Current time and date: {formatted_date},{formatted_time}\nItem back in stock go to \n{url}",
    #         )
    #     if x % 60 == 0:
    #         time.sleep(1)
    #         item_status = (
    #             "Back in Stock" if btn_inner_text == "Add to Cart" else btn_inner_text
    #         )
    #         # send_message(
    #         #     "2242458826",
    #         #     "8473854005",
    #         #     "att",
    #         #     f"Update on item: {item_status} \n {url}",
    #         # )
    #         send_message_one(
    #             "2242458826",
    #             "att",
    #             f"Current time: {formatted_date},{formatted_time}\nUpdate on item: {item_status} \n {url}",
    #         )
    #     print("refreshing...")
    #     driver.refresh()
    #     print("refreshed")
    #     x += 1
    #     print("refresh " + str(x))


def test_site():
    print("Loading test site")
    driver.get("https://www.google.com")
    time.sleep(5)
    print(f"On Test Site: {driver.current_url}")
    print("Testing refresh...")
    driver.refresh()
    time.sleep(3)
    print(f"Refresh Complete. \n On {driver.current_url}")
    logo = driver.find_elements(by=By.CLASS_NAME, value="lnXdpd")
    if len(logo) == 1:
        print("Test passed: Logo found")
    else:
        print("Test failed: Logo not found!")
    driver.quit()
