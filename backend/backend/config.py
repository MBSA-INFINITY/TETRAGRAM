import os


class Config:
    secret_key = os.path.join(os.path.dirname(os.path.abspath(__file__)), "key.json")
    firebase_web_api_key = 'AIzaSyAuTj0D32-B3CJ6eiHJ-OnHGNQNBtEwytM'
    login_endpoint = f'https://identitytoolkit.googleapis.com/v1/accounts:signInWithPassword?key={firebase_web_api_key}'
    register_endpoint = f'https://identitytoolkit.googleapis.com/v1/accounts:signUp?key={firebase_web_api_key}'
