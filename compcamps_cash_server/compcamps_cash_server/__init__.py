from flask import Flask

import os
from pymongo import MongoClient
from dotenv import load_dotenv, find_dotenv

# Initialize connection to MongoDB database
load_dotenv(find_dotenv())
client = MongoClient(os.getenv("MONGO_URL"),
                      username=os.getenv("MONGO_USERNAME"),
                      password=os.getenv("MONGO_PASSWORD"),
                      authSource=os.getenv("MONGO_AUTHSOURCE"),
                      authMechanism='SCRAM-SHA-1')
db = client.heroku_1q0qc73n

template_dir = os.path.abspath('./views')
app = Flask(__name__, template_folder='views', static_url_path=template_dir)
prefix = "000000"


import compcamps_cash_server.routes