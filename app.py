from flask import Flask, render_template, request
from adder import *

app = Flask(__name__)

@app.route("/", methods = ["GET", "POST"])
def index():
    if request.method == "POST":
        num1 = "0" + request.form.get("num1")
        num2 = "0" + request.form.get("num2")
        mode = int(request.form.get("operasi"))

        if mode == 2:
            num2 = inverter(num2[1:])

        result = adder(num1,num2)
        
        if result[1] == "1" and num1[1] == "0" and num2[1] == "0":
            result = "Overflow!!"
        elif result[1] == "0" and num1[1] == "1" and num2[1] == "1":
            result = "Overflow!!"
        else:
            result = result[1:]
        return render_template("index.html", result=result)

    return render_template("index.html")