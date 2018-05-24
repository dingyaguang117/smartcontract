#coding=utf-8
__author__ = 'ding'

import yobit

MARKETS = [
    ('yobit', yobit),
]




def check_all_markets(currency):
    ret = {}
    for market in MARKETS:
        name, package = market
        ret[name] = package.check_currency(currency)
    return ret



if __name__ == '__main__':
    print check_all_markets('BTC')