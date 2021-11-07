from flask import Flask, render_template
import json
from coinbase.wallet.client import Client

app = Flask(__name__)


@app.route('/')
def mainpage():
    return render_template('main.html')


def get_coinbase_prices(coin):
	data = get_keys()
	client = Client(data["coinbase_key"], ["coinbase_secret"])

    return 0, 0


def get_keys():
    with open('secrets.json') as json_file:
        data = json.load(json_file)
    return data
