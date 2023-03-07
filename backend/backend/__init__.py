from flask import Flask, request, jsonify
from firebase_admin import credentials, firestore, initialize_app # Initialize Flask App
from backend.config import Config


app = Flask(__name__)# Initialize Firestore DB
cred = credentials.Certificate(Config.secret_key)
default_app = initialize_app(cred)
db = firestore.client()

from backend.users.routes import users

app.register_blueprint(users)