import click
import json
from currency_converter import CurrencyConverter # better library is maybe forex-python==1.1
from collections import OrderedDict

### Load the packaged data (might not be up to date). ###
## For up to date data insert the latest data source between parenthesis ##
c = CurrencyConverter('./eurofxref-hist.csv', fallback_on_wrong_date=True)

def converted_currency(amount, input_currency, output_currency):
    if output_currency != None:
        converted_one_currency = c.convert(amount, input_currency, output_currency)
        return {output_currency: converted_one_currency}
    else:
        dict_of_currencies = {}
        for currency in c.currencies:
            converted_more_currencies = c.convert(amount, input_currency, currency)
            data = {currency: converted_more_currencies}
            dict_of_currencies.update(data)
        sorted_dict = OrderedDict(sorted(dict_of_currencies.items()))
        return sorted_dict


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
        "output": converted_currency(amount, input_currency, output_currency)
    }
    click.echo(json.dumps(data, indent=4))

if __name__ == '__main__':
    converter()
