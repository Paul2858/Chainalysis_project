from flask import Flask, render_template, jsonify, request
import json
import os
import signal
import shrimpy
from utils import build_price_dic, get_rec

app = Flask(__name__)


@app.route('/stopServer', methods=['GET'])
def stopServer():
    os.kill(os.getpid(), signal.SIGINT)
    return jsonify({"success": True, "message": "Server is shutting down..."})


@app.route('/')
def mainpage():
    prices = build_price_dic()
    reco = get_rec(prices)
    return render_template('main.html', p=prices, recs=reco)
