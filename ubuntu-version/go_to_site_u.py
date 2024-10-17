from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options

from send_text_u import send_message_one, send_message
from refresh_page import countdown

import time

import datetime
from datetime import timedelta

# Get the current date and time
now = datetime.datetime.now() - timedelta(hours=5)

# Format the date and time
formatted_date = now.strftime("%A, %B %d, %Y")
formatted_time = now.strftime("%I:%M %p")

service = Service(
    log_output="geckodriver.log",
    executable_path="/usr/local/bin/geckodriver",
)
options = Options()
options.add_argument("--headless")
driver = webdriver.Firefox(options=options, service=service)

limit = 1000
my_num = "2242458826"
kayla_num = "8473854005"


def go_to_site(url):
    driver.get(url)
    print(f"On {url}")
    current_time = f"{formatted_date} at, {formatted_time}"
    send_message(
        my_num,
        kayla_num,
        "att",
        f"Program Started on {current_time}",
    )
    time.sleep(2)
    add_to_cart_btn = driver.find_element(by=By.ID, value="product-addtocart-button")
    btn_inner_text = add_to_cart_btn.get_attribute("innerText").strip()
    print(btn_inner_text)
    # inner text: Out Of Stock
    print("STARTING REFRESH PHASE...")
    for x in range(0, limit):
        countdown(int(60))
        if btn_inner_text != "Out Of Stock":
            time.sleep(1)
            send_message(my_num, kayla_num, "att", f"Item back in stock go to \n{url}")
            # send_message_one(
            #     my_num,
            #     "att",
            #     f"ITEM BACK IN STOCK HURRY GO TO: \n{url}\nCurrent time: {current_time}",
            # )
        if x % 2 == 0:
            time.sleep(1)
            item_status = (
                "Back in Stock" if btn_inner_text == "Add to Cart" else btn_inner_text
            )
            send_message(
                my_num, kayla_num, "att", f"Update on item: {item_status} \n {url}"
            )
            # send_message_one(
            #     my_num,
            #     "att",
            #     f"Current time: {current_time}\nUpdate on item: {item_status} \n {url}",
            # )
        print("refreshing...")
        driver.refresh()
        x += 1
        print(f"refresh {x}")


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
