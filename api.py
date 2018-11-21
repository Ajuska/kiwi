from flask import Flask, jsonify, request
from currency_converter import converter, convert_currency, get_code


app = Flask(__name__)
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True


@app.route('/')
def index():
    return 'Welcome to currency converter!'

# /currency_converter?amount=100.0&input_currency=EUR&output_currency=CZK
@app.route('/api/v1/currency_converter')
def api_converter():
    amount = request.args.get('amount', '')
    input_currency = request.args.get('input_currency', '')
    output_currency = request.args.get('output_currency', None)
    if len(input_currency) <= 2:
        input_currency = get_code(input_currency)
    if output_currency != None:
        if len(output_currency) <= 2:
            output_currency = get_code(output_currency)
    data =  {
                "input": {
                    "amount": amount,
                    "currency": input_currency
                },
                "output": convert_currency(amount, input_currency, output_currency)
            }
    return jsonify(data)



if __name__ == '__main__':
    app.run()
