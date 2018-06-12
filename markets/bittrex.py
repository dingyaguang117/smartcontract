#coding=utf-8
__author__ = 'ding'
import traceback
import requests
import json

def check_currency(currency):
    url = 'https://bittrex.com/api/v1.1/public/getcurrencies'
    try:
        content = requests.get(url).content
        result = json.loads(content)
        if not result['success']:
            return result['message']
        for item in result['result']:
            if item['Currency'] == currency:
                return True
        return False
    except:
        print traceback.format_exc()
        return 'Error'



if __name__ == '__main__':
    print check_currency('BCD')