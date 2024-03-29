from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import scrape_mars

app = Flask(__name__)

mongo = PyMongo(app, uri="mongodb://localhost:27017/mars_app")


@app.route("/")
def home():

    destination_data = mongo.db.collection.find_one()

    return render_template("index.html", datas=space_data)


@app.route("/scrape")
def scrape():

    mars_data = mars_scrape.scrape_info()

    mongo.db.collection.update({}, mars_data, upsert=True)

    # Redirect back to home page
    return redirect("/")


if __name__ == "__main__":
    app.run(debug=True)
