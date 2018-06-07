import json
import time

from flask import Flask
from markets import check_all_markets

app = Flask(__name__)


@app.route('/')
def _index():
    return index("BTC")


@app.route('/<currency>')
def index(currency="BTC"):
    print currency
    data = {
        'currency': currency,
    }
    result = check_all_markets(currency)
    data['markets'] = result
    data['done'] = 'no'
    for v in result.values():
        if v == True:
            data['done'] = "yes"
            break
    data['timestamp'] = time.time()
    return json.dumps(data)


if __name__ == '__main__':
    app.run(port=8000)
