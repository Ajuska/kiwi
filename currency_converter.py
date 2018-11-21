import click
import json
from forex_python.converter import CurrencyRates
from aja_convert import CurrencyCodes
from collections import OrderedDict
import requests


@click.command()
@click.option('--amount', '-a',
                help='Amount you want to convert')
@click.option('--input_currency', '-i',
                help='Input currrency format')
@click.option('--output_currency', '-o',
                help='Output currency format')
def converter(amount, input_currency, output_currency):
    if len(input_currency) <= 2:
        input_currency = get_code(input_currency)
    if output_currency != None:
        if len(output_currency) <= 2:
            output_currency = get_code(output_currency)
    data = {
        "input": {
            "amount": amount,
            "currency": input_currency
        },
        "output": convert_currency(amount, input_currency, output_currency)
    }
    click.echo(json.dumps(data, indent=4))


def get_code(symbol):
    s = CurrencyCodes()
    if symbol == '£':
        symbol = 'GBP'
    elif symbol == '$':
        symbol = 'USD'
    else:
        symbol = s.get_currency_code_from_symbol(symbol)
    return symbol


def create_offline_converter():
    return CurrencyRates()


def convert_currency(amount, input_currency, output_currency):
    c = create_offline_converter()

    currencies_to_convert = []

    if output_currency == None:
        get_currencies = requests.get('https://ratesapi.io/api/latest').text
        currencies = json.loads(get_currencies).get('rates', {})
        currencies.update({'EUR': 1})
        for currency in currencies:
            currencies_to_convert.append(currency)
    else:
        currencies_to_convert.append(output_currency)

    dict_of_rates = {}
    for currency in currencies_to_convert:
        conv_amount = c.convert(input_currency, currency, float(amount))
        dict_of_rates.update({currency: round(conv_amount, 2)})

    return OrderedDict(sorted(dict_of_rates.items()))


if __name__ == '__main__':
    converter()
