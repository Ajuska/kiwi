## Kiwi project for junior python developer

The project is based on [Kiwi practical task](https://gist.github.com/MichalCab/c1dce3149d5131d89c5bbddbc602777c).

Please install all dependencies in requirement.txt file to run this project.

# CLI

To run the Command Line Interface type:
`python3 money_converter.py --amount 100.0 --input_currency EUR --output_currency CZK`

The response will be:
```
{   
    "input": {
        "amount": 100.0,
        "currency": "EUR"
    },
    "output": {
        "CZK": 2601.3,
    }
}
```

# API

To run the Application Programming Interface type in the command line:
`python3 api.py`

After, type the API endpoint.
`http://127.0.0.1:5000/api/v1/currency_converter?amount=100.0&input_currency=EUR&output_currency=CZK`

The response will be:
```
{   
    "input": {
        "amount": 100.0,
        "currency": "EUR"
    },
    "output": {
        "CZK": 2601.3,
    }
}
```
