import json
import time

from flask import Flask
from markets import check_all_markets

app = Flask(__name__)

CURRENCY = 'BTC'


@app.route('/')
def index():
    data = {
        'currency': CURRENCY,
    }
    result = check_all_markets(CURRENCY)
    data['markets'] = result
    data['done'] = any(result.values())
    data['timestamp'] = time.time()

    return json.dumps(data)


if __name__ == '__main__':
    app.run(port=8000)
