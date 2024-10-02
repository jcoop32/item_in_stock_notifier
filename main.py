from go_to_site import go_to_site


def item_in_stock_notifier(url):
    go_to_site(url)


item_in_stock_notifier(
    "https://www.usa.canon.com/shop/p/powershot-g7-x-mark-ii?color=Black&type=New"
)
