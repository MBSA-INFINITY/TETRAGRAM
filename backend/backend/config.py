import os

class Config:
    secret_key = os.path.join(os.path.dirname(os.path.abspath(__file__)),"key.json")
