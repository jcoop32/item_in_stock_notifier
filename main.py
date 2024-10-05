from go_to_site import go_to_site, test_site
import sys


def item_in_stock_notifier(url):
    go_to_site(url)


if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "test":
        test_site()
    else:
        print("No Test Request...")
        item_in_stock_notifier(
            "https://www.usa.canon.com/shop/p/powershot-g7-x-mark-ii?color=Black&type=New"
        )
