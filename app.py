from urllib.parse import quote_plus
from flask import Flask, render_template
from pymongo import MongoClient
from dotenv import load_dotenv
from flask import jsonify
import os
from pymongo.errors import PyMongoError

app = Flask(__name__)

load_dotenv() #load env variables from .env files

MONGODB_USERNAME = os.getenv('MONGODB_USERNAME')
MONGODB_PASSWORD = os.getenv('MONGODB_PASSWORD')

print("USername = "+str(MONGODB_USERNAME))
print("MONGODB_PASSWORD"+str(MONGODB_PASSWORD))
# URL-encode the username and password

encoded_username = quote_plus(MONGODB_USERNAME)
encoded_password = quote_plus(MONGODB_PASSWORD)

client = MongoClient(f"mongodb+srv://myuser:{encoded_password}@cluster0.tf8t0.mongodb.net/shop_db?retryWrites=true&w=majority&tls=true")
db = client.shop_db
products_collection = db["products"]

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/products')
def products():
    try:
        products = list(products_collection.find())
        # Return the products in the template
        return render_template('products.html', products=products)
    except PyMongoError as e:
        # Handle any MongoDB related errors
        app.logger.error(f"Database error: {e}")
        return jsonify({"error": "Database error occurred, please try again later."}), 500
    except Exception as e:
        # Catch other unexpected errors
        app.logger.error(f"Unexpected error: {e}")
        return jsonify({"error": "An unexpected error occurred, please try again later."}), 500

if __name__ == '__main__':
    app.run(debug=True)


