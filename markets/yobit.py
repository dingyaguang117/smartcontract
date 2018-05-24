#coding=utf-8
__author__ = 'ding'
import traceback
import requests
from lxml import etree

def check_currency(currency):
    url = 'https://yobit.net/en/market/'
    try:
        content = requests.get(url).content
        tree = etree.HTML(content)
        trades = tree.xpath('//table[@id="market_table"]//a/text()')
        for trade in trades:
            c1, c2 = trade.split('/')
            if c1 == currency or c2 == currency:
                return True
        return False
    except:
        print traceback.format_exc()
        return 'Error'



if __name__ == '__main__':
    print check_currency('BTC')