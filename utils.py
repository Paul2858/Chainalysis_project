

def build_price_dic():
    btc_a_cb, btc_b_cb = get_prices("coinbasepro", "BTC")
    btc_a_bi, btc_b_bi = get_prices("binanceus", "BTC")

    eth_a_cb, eth_b_cb = get_prices("coinbasepro", "ETH")
    eth_a_bi, eth_b_bi = get_prices("binanceus", "ETH")
    dic = {
        "coinbase": {"BTC": {"ask": btc_a_cb, "bid": btc_b_cb}, "ETH": {"ask": eth_a_cb, "bid": eth_b_cb}},
        "binance": {"BTC": {"ask": btc_a_bi, "bid": btc_b_bi}, "ETH": {"ask": eth_a_bi, "bid": eth_b_bi}}
    }
    return dic


def get_rec(prices):

    rec = {}

    if prices["coinbase"]["BTC"]["bid"] == "UNAVAILABLE":
        rec["BTC-buy-rec"] = "UNAVAILABLE"
        rec["ETH-sell-rec"] = "UNAVAILABLE"
        rec["BTC-buy-rec"] = "UNAVAILABLE"
        rec["ETH-sell-rec"] = "UNAVAILABLE"
        return rec

    if prices["coinbase"]["BTC"]["ask"] < prices["binance"]["BTC"]["ask"]:
        BTC_ask_rec = "Coinbase"
    else:
        BTC_ask_rec = "Binance"

    rec["BTC-buy-rec"] = BTC_ask_rec

    if prices["coinbase"]["ETH"]["ask"] < prices["binance"]["ETH"]["ask"]:
        ETH_ask_rec = "Coinbase"
    else:
        ETH_ask_rec = "Binance"

    rec["ETH-buy-rec"] = ETH_ask_rec

    if prices["coinbase"]["ETH"]["bid"] > prices["binance"]["ETH"]["bid"]:
        ETH_bid_rec = "Coinbase"
    else:
        ETH_bid_rec = "Binance"

    rec["ETH-sell-rec"] = ETH_bid_rec

    if prices["coinbase"]["BTC"]["bid"] > prices["binance"]["BTC"]["bid"]:
        BTC_bid_rec = "Coinbase"
    else:
        BTC_bid_rec = "Binance"

    rec["BTC-sell-rec"] = BTC_bid_rec

    return rec


def get_keys():
    with open('secrets.json') as json_file:
        data = json.load(json_file)
    return data["public"], data["secret"]


def shrimpy_api():
    public, secret = get_keys()
    return shrimpy.ShrimpyApiClient(public, secret)


def get_prices(exchange, crypto):
    client = shrimpy_api()
    orderbook = client.get_orderbooks(
        exchange,  # exchange: ex:'coinbasepro'
        crypto,      # base_symbol
        'USD',      # quote_symbol
        1          # limit
    )
    if not orderbook[0]["orderBooks"][0]["orderBook"]:
        return "UNAVAILABLE", "UNAVAILABLE"

    try:
        print(orderbook[0]["orderBooks"][0]["orderBook"]["asks"][0]["price"])
        print()
        ask = orderbook[0]["orderBooks"][0]["orderBook"]["asks"][0]["price"]
        bid = orderbook[0]["orderBooks"][0]["orderBook"]["bids"][0]["price"]
    except RuntimeError:
        ask = "UNAVAILABLE"
        bid = "UNAVAILABLE"
        print("Error with data")
    return ask, bid
