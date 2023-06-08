from flask import Flask, render_template , request

app = Flask(__name__)

@app.route("/home/")
def home():
    return render_template("home.html")

@app.route("/about/")
def about():
    return render_template("about.html")

@app.route("/all/")
def all():
    page=request.args.get("page")
    return render_template(page)

@app.route("/introduction/")
def introduction():
    page=request.args.get("name")
    return  render_template("introduction.html",p=page)

