import click
import json
from currency_converter import CurrencyConverter # better library is maybe forex-python==1.1
from collections import OrderedDict


@click.command()
@click.option('--amount', '-a',
                help='Amount you want to convert')
@click.option('--input_currency', '-i',
                help='Input currrency format')
@click.option('--output_currency', '-o',
                help='Output currency format')
def converter(amount, input_currency, output_currency):
    data = {
        "input": {
            "amount": amount,
            "currency": input_currency
        },
        "output": convert_currency(amount, input_currency, output_currency)
    }
    click.echo(json.dumps(data, indent=4))

def create_offline_converter():
    ### Load the packaged data (might not be up to date). ###
    ## For up to date data insert the latest data source between parenthesis ##
    return CurrencyConverter('./eurofxref-hist.csv', fallback_on_wrong_date=True)

def convert_currency(amount, input_currency, output_currency):
    c = create_offline_converter()

    if output_currency == None:
        currencies_to_convert = c.currencies
    else:
        currencies_to_convert = { output_currency, }

    dict_of_currencies = {}
    for currency in currencies_to_convert:
        converted_amount = c.convert(amount, input_currency, currency)
        dict_of_currencies.update({currency: round(converted_amount, 2)})

    return OrderedDict(sorted(dict_of_currencies.items()))


if __name__ == '__main__':
    converter()
