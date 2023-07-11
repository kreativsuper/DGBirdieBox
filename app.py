from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/home")
def home():
    return render_template("index.html")

@app.route("/support")
def support():
    return render_template("support.html")

@app.route("/privacy")
def privacy():
    return render_template("privacy.html")

@app.route("/business")
def business():
    return render_template("business.html")

@app.route("/apps")
def apps():
    return render_template("apps.html")

