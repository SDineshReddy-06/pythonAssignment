from flask import Flask, render_template, request, redirect
from pymongo import MongoClient

app = Flask(__name__)
client = MongoClient("mongodb+srv://sdreddy786:uprGBHOQTElk6lEK@cluster0.ohqybxv.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
db = client["studentDetails"]
collection = db["studentDetailsCollection"]

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/details", methods=["POST"])
def details():
    name = request.form["name"]
    email = request.form["email"]
    city = request.form["city"]
    number = request.form["number"]
    grade = request.form["grade"]
    collection.insert_one({"name":name, "email":email, "city":city, "number":number, "grade":grade})
    return redirect("/studentDetails")

@app.route("/studentDetails")
def studentDetails():
    all_details = list(collection.find())
    return render_template("studentDetails.html",details=all_details )

if __name__ == "__main__":
    app.run(debug=True)