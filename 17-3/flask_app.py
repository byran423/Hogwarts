from flask import Flask, escape, request, session


app = Flask(__name__)
app.secret_key = "yangbai"


@app.route("/")
def hello():
    name = request.args.get("name", "World")
    return f"Hello, {escape(name)}!"


@app.route("/login", methods=["POST", "GET"])
def login():
    res = {
        "method": request.method,
        "url": request.url,
        "args": request.args,
        "form": request.form,
    }
    session["username"] = request.args.get("name")
    return res
