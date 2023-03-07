from flask import Blueprint, request
import json
import requests
from backend.config import Config
from backend import db

users = Blueprint('users', __name__)
users_ref = db.collection('users')

@users.route('/register', methods=['POST'])
def register():
    """
        register() : Register a new user
    """
    try:
        # Check for ID in URL query
        payload = {
            'email': request.json['email'],
            'password': request.json['password']
        }
        user = requests.post(Config.register_endpoint, data=json.dumps(payload))
        users_ref.add(payload)
        return user.json(), 200
    except Exception as e:
        return f"An Error Occurred: {e}"


@users.route('/login', methods=['POST'])
def login():
    payload = {
        'email': request.json['email'],
        'password': request.json['password'],
        'returnSecureToken': True
    }

    response = requests.post(Config.login_endpoint, data=json.dumps(payload))
    return response.json()
