import json

import requests

APIKEY = ""
VENUE = ""
STOCK = ""
BASE_URL = "https://api.stockfighter.io/ob/api"

ACCOUNT = ""


def buy(price, qty, venue=VENUE, symbol=STOCK, account=ACCOUNT, order_type="limit"):
    order = {
        "account": account,
        "venue": venue,
        "symbol": symbol,
        "price": price,
        "qty": qty,
        "direction": "buy",
        "orderType": order_type
    }

    return send_post_request(order, venue, symbol).json()


def send_post_request(order, venue, stock):
    url = BASE_URL + "/venues/{venue}/stocks/{stock}/orders".format(venue=venue, stock=stock)
    r = requests.post(url, data=json.dumps(order), headers={"X-Starfighter-Authorization": APIKEY})
    return r


def heartbeat_venue(venue=VENUE):
    url = BASE_URL + "/venues/{venue}/heartbeat".format(venue=venue)
    r = requests.get(url, headers={"X-Starfighter-Authorization": APIKEY})
    return r.json().get("ok")


def list_stocks(venue=VENUE):
    url = BASE_URL + "/venues/{venue}/stocks".format(venue=venue)
    r = requests.get(url, headers={"X-Starfighter-Authorization": APIKEY})
    if r.json().get("ok"):
        for i in r.json().get("symbols"):
            yield i
    return None


def quote(stock, venue=VENUE):
    url = BASE_URL + "/venues/{venue}/stocks/{stock}/quote".format(venue=venue, stock=stock)
    r = requests.get(url, headers={"X-Starfighter-Authorization": APIKEY})
    if r.json().get("ok"):
        return r.json()
    return None


def get_price(stock, venue=VENUE):
    res = quote(stock, venue)
    return res.get("bid")


def status_all_orders(venue=VENUE, account=ACCOUNT):
    url = BASE_URL + "/venues/{venue}/accounts/{account}/orders".format(venue=venue, account=account)
    r = requests.get(url, headers={"X-Starfighter-Authorization": APIKEY})
    if r.json().get("ok"):
        for i in r.json().get("orders"):
            yield i
    return None


def status_one_order(stock, order_id, venue=VENUE):
    url = BASE_URL + "/venues/{venue}/stocks/{stock}/orders/{id}".format(venue=venue, stock=stock, id=order_id)
    r = requests.get(url, headers={"X-Starfighter-Authorization": APIKEY})
    if r.json().get("ok"):
        return r.json()
    return None


def buy_100k():
    for cnt in range(10000):
        prc = 7050
        res = get_price(STOCK)
        if res is None:
            res = prc + 1
        print(res)
        if res < prc:
            print(buy(prc, 5000, order_type="immediate-or-cancel"))


if __name__ == "__main__":
    # print(heartbeat_venue())
    # first_stock = next(list_stocks())
    # print(quote(first_stock.get("symbol")))
    buy_100k()
