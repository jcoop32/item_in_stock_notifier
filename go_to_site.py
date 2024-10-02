from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service

from selenium.webdriver.firefox.options import Options

# from selenium.webdriver.chrome.options import Options

from send_text import send_message_one, send_message
from refresh_page import countdown

import time


service = Service(
    executable_path="/Users/joshcooper/item_in_stock_notifier/chromedriver"
)
options = Options()
options.add_argument("--headless")

driver = webdriver.Firefox(options=options)
# driver = webdriver.Firefox()
# driver = webdriver.Chrome()

limit = 1000


def go_to_site(url):
    driver.get(url)
    print(f"On {url}")
    send_message_one("2242458826", "att", f"Program Started, On {url}")
    time.sleep(2)
    add_to_cart_btn = driver.find_element(by=By.ID, value="product-addtocart-button")
    btn_inner_text = add_to_cart_btn.get_attribute("innerHTML")
    print(f"Inner Text: {btn_inner_text}")
    print("STARTING REFRESH PHASE...")
    for x in range(0, limit):
        countdown(int(10))
        if btn_inner_text != "Out Of Stock":
            time.sleep(1)
            send_message(
                "2242458826", "8473854005", "att", f"Item back in stock go to \n{url}"
            )
        if x % 3 == 0:
            time.sleep(1)
            item_status = (
                "Back in Stock" if btn_inner_text == "Add to Cart" else btn_inner_text
            )
            send_message(
                "2242458826",
                "8473854005",
                "att",
                f"Update on item: {item_status} \n {url}",
            )
        print("refreshing...")
        driver.refresh()
        print("refreshed")
        x += 1
        print("refresh " + str(x))
