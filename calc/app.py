# Put your app in here.

from flask import Flask, request
from operations import add, sub, mult, div

app = Flask(__name__)

@app.route('/add')
def calc_add():
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    equals = str(add(a,b))
    return equals

@app.route('/sub')
def calc_sub():
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    equals = str(sub(a,b))
    return equals

@app.route('/mult')
def calc_mult():
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    equals = str(mult(a,b))
    return equals

@app.route('/div')
def calc_div():
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    equals = str(div(a, b))
    return equals