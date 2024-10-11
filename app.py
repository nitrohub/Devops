from urllib.parse import quote_plus
from flask import Flask, render_template
from pymongo import MongoClient

app = Flask(__name__)

username = "c0901466"  # replace with your actual username
password = "G@9a*HH2XSYqCC6"  # replace with your actual password

# # URL-encode the username and password
encoded_username = quote_plus(username)
encoded_password = quote_plus(password)

# Connect to MongoDB Atlas
client = MongoClient(f"mongodb+srv://{encoded_username}:{encoded_password}@cluster0.9bcht.mongodb.net/shop_db?retryWrites=true&w=majority&tls=true")

db = client.shop_db
products_collection = db.products

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/products')
def products():
    print("Aagaya*****************************")
    products = products_collection.find()
    # print("After Products="+str(len(products)))
    # for i in products:
    #     print(i)
    return render_template('products.html', products=products)

if __name__ == '__main__':
    app.run(debug=True)

# from pymongo import MongoClient

# # Replace <username>, <password>, and <dbname> with your values
# client = MongoClient("mongodb+srv://encoded_username:encoded_password@cluster0.9bcht.mongodb.net/shop_db?retryWrites=true&w=majority&tls=true")

# # Test connection
# try:
#     client.admin.command('ping')
#     print("Connected successfully!")
# except Exception as e:
#     print("Could not connect to MongoDB:", e)


