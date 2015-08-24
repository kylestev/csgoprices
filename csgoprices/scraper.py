import functools
from requests_futures.sessions import FuturesSession
from csgoprices import responses

__ALL__ = ['Scraper', 'Currencies']

SESSION = FuturesSession()
URL_MARKET_PRICE_OVERVIEW = 'https://steamcommunity.com/market/priceoverview/'


def response(func):
    def wrap(func):
        @functools.wraps(func)
        def response_decorator(*args, **kwargs):
            content = func(*args, **kwargs).result().content
            return responses.SteamPriceResponseParser(content).parse()
        return response_decorator
    return wrap(func)


class Currency(object):
    def __init__(self, id, name, symbol):
        self.id = id
        self.name = name
        self.symbol = symbol


class Currencies(object):
    USD = Currency(1, 'USD', '$')
    GBP = Currency(2, 'GBP', u'\xc2')
    EUR = Currency(3, 'EUR', u'\xe2')


class Scraper(object):
    def __init__(self, appid = 730, currency = Currencies.USD):
        self.appid = appid
        self.currency = currency

    @response
    def build_request(self, item_name):
        params = {'appid': self.appid, 'currency': self.currency.id,
                  'market_hash_name': item_name}
        return SESSION.get(URL_MARKET_PRICE_OVERVIEW, params=params)
