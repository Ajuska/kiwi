# this file is to be subsituted by new version of forex_python
# it is the copy og the CurrencyCodes class
# they did not accept my change request yet, symbol converting is not in package for now
import os
import simplejson as json

class CurrencyCodes:

    def __init__(self):
        pass

    def _get_data(self, currency_code):
        file_path = os.path.dirname(os.path.abspath(__file__))
        with open(file_path+'/raw_data/currencies.json') as f:
            currency_data = json.loads(f.read())
        currency_dict = next((item for item in currency_data if item["cc"] == currency_code), None)
        return currency_dict

    def _get_data_from_symbol(self, symbol):
        file_path = os.path.dirname(os.path.abspath(__file__))
        with open(file_path + '/raw_data/currencies.json') as f:
            currency_data = json.loads(f.read())
        currency_dict = next((item for item in currency_data if item["symbol"] == symbol), None)
        return currency_dict

    def get_symbol(self, currency_code):
        currency_dict = self._get_data(currency_code)
        if currency_dict:
            return currency_dict.get('symbol')
        return None

    def get_currency_name(self, currency_code):
        currency_dict = self._get_data(currency_code)
        if currency_dict:
            return currency_dict.get('name')
        return None

    def get_currency_code_from_symbol(self, symbol):
        currency_dict = self._get_data_from_symbol(symbol)
        if currency_dict:
            return currency_dict.get('cc')
        return None


_CURRENCY_CODES = CurrencyCodes()


get_symbol = _CURRENCY_CODES.get_symbol
get_currency_name = _CURRENCY_CODES.get_currency_name
get_currency_code_from_symbol = _CURRENCY_CODES.get_currency_code_from_symbol
