from urllib.parse import quote_plus
from flask import Flask, render_template
from pymongo import MongoClient
from dotenv import load_dotenv
import os

app = Flask(__name__)

load_dotenv() #load env variables from .env files

MONGODB_USERNAME = os.getenv('MONGODB_USERNAME')
MONGODB_PASSWORD = os.getenv('MONGODB_PASSWORD')

# URL-encode the username and password

encoded_username = quote_plus(MONGODB_USERNAME)
encoded_password = quote_plus(MONGODB_PASSWORD)

# Connect to MongoDB Atlas
client = MongoClient(f"mongodb+srv://{encoded_username}:{encoded_password}@cluster0.9bcht.mongodb.net/shop_db?retryWrites=true&w=majority&tls=true")

db = client.shop_db
products_collection = db.products

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/products')
def products():
    products = products_collection.find()
    return render_template('products.html', products=products)

if __name__ == '__main__':
    app.run(debug=True)


