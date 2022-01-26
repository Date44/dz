from flask import Flask
from pymongo import MongoClient

app = Flask(__name__)
app.config['SECRET_KEY'] = '872b40d642e43b9788750c96999938fc'
app.config['TEMPLATES_AUTO_RELOAD'] = True

client = MongoClient("mongodb+srv://Date44:maksim2005@cluster1.4pskb.mongodb.net/webshop_db?retryWrites=true&w=majority")
db = client.webshop_db
