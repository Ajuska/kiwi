from flask import Flask, jsonify, request
from money_converter import converter, converted_currency


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
    data =  {
                "input": {
                    "amount": amount,
                    "currency": input_currency
                },
                "output": converted_currency(amount, input_currency, output_currency)
            }
    return jsonify(data)



if __name__ == '__main__':
    app.run(debug=True)
