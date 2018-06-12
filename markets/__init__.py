#coding=utf-8
__author__ = 'ding'

import yobit
import bittrex

MARKETS = {
    'yobit': yobit,
    'bittrex': bittrex
}


def check_market(market, currency):
    ret = {}
    if market not in MARKETS:
        ret[market] = 'market not support'
        return ret

    package = MARKETS[market]
    ret[market] = package.check_currency(currency)
    return ret


def check_all_markets(currency):
    ret = {}
    for name in MARKETS:
        ret[name] = MARKETS[name].check_currency(currency)
    return ret



if __name__ == '__main__':
    print check_all_markets('LTC')