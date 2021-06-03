import flask
from flask import Flask
from flask_pymongo import PyMongo
from dotenv import load_dotenv
load_dotenv()
import os


app = Flask(__name__)

mongodb_client = PyMongo(app, uri={os.getenv("MONGO_URL")})

@app.route('/get-update', methods=['GET'])
def handle_update():
    return {
        'status': "/get-update",
        'message': "active serve"
    }


@app.route('/', methods=['GET'])
def hello_world():
    return {
        'status': "API is active and Live!",
        'pythonversion': "latest"
    }


@app.route('/get-db', methods=['GET'])
def get_from_db():
    try:
        recipes = mongodb_client.SIT.find({})
        print(recipes)
        return flask.jsonify([recipe for recipe in recipes])
    except:
        print("error")


if __name__ == '__main__':
    app.run()

