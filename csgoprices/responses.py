import json
from csgoprices import utils
from csgoprices import errors

__ALL__ = ['SteamPriceResponseParser']

def currency_cleaner(value):
    return int(float(value[1:]) * 100)

def number_cleaner(value):
    return int(value.replace(',', ''))

class SteamPriceResponseParser(object):
    def __init__(self, response):
        self.response = response

    def parse(self):
        body = json.loads(self.response)
        if not body['success']:
            raise errors.APIResponseFailure(body=self.response)
        del body['success']
        for (key, value) in body.items():
            if '_price' in key:
                value = currency_cleaner(value)
            elif 'volume' == key:
                value = number_cleaner(value)
            body[key] = value
        return SteamPriceResponse(**body)

class SteamPriceResponse(object):
    def __init__(self, **kwargs):
        for k, v in kwargs.items():
            setattr(self, k, v)

    def __str__(self):
        return utils.obj_str(self)

