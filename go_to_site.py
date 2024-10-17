from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.firefox.options import Options

from send_text import send_message_one, send_message
from refresh_page import countdown

import time
import datetime


service = Service(
    log_output="geckodriver.log",
    executable_path="/Users/joshcooper/item_in_stock_notifier/geckodriver",
)
options = Options()
options.add_argument("--headless")
driver = webdriver.Firefox(options=options)
# driver = webdriver.Firefox()

limit = 1000

now = datetime.datetime.now()

# Format the date and time
formatted_date = now.strftime("%A, %B %d, %Y")
formatted_time = now.strftime("%I:%M %p")


def go_to_site(url):
    driver.get(url)
    print(f"On {url}")
    print(formatted_date)
    print(formatted_time)
    # send_message_one("2242458826", "att", f"Program Started, On {url}")
    time.sleep(2)
    add_to_cart_btn = driver.find_element(by=By.ID, value="product-addtocart-button")
    btn_inner_text = add_to_cart_btn.get_attribute("innerText").strip()
    print(btn_inner_text)
    # inner text is OUT OF STOCK
    print("STARTING REFRESH PHASE...")
    for x in range(1, limit):
        countdown(int(180))
        if btn_inner_text != "OUT OF STOCK":
            time.sleep(1)
            # send_message(
            #     "2242458826", "8473854005", "att", f"Item back in stock go to \n{url}"
            # )
            # send_message_one("2242458826", "att", f"Item back in stock go to \n{url}")
            print("Item back in stock")
        if x % 60 == 0:
            time.sleep(1)
            item_status = (
                "Back in Stock" if btn_inner_text == "Add to Cart" else btn_inner_text
            )
            # send_message(
            #     "2242458826",
            #     "8473854005",
            #     "att",
            #     f"Update on item: {item_status} \n {url}",
            # )
            # send_message_one(
            #     "2242458826", "att", f"Update on item: {item_status} \n {url}"
            # )
            print(f"Item update: {item_status}")
        print("refreshing...")
        driver.refresh()
        x += 1
        print("refresh " + str(x))


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
