from flask import Flask, request

# Import the functions from the operations module
from operations import add, sub, mult, div

app = Flask(__name__)

@app.route('/add')
def add_route():
    a = request.args.get('a')
    b = request.args.get('b')
    result = add(a, b)
    return str(result)

@app.route('/sub')
def sub_route():
    a = request.args.get('a')
    b = request.args.get('b')
    result = sub(a, b)
    return str(result)

@app.route('/mult')
def mult_route():
    a = request.args.get('a')
    b = request.args.get('b')
    result = mult(a, b)
    return str(result)

@app.route('/div')
def div_route():
    a = request.args.get('a')
    b = request.args.get('b')
    result = div(a, b)
    return str(result)

if __name__ == '__main__':
    app.run()