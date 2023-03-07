from flask import Blueprint, request
from backend import db

members = Blueprint('members', __name__)
members_ref = db.collection('members')

@members.route('/add', methods=['POST'])
def add():
    try:
        payload = {
            'name': request.json['name'],
            'roll': request.json['roll'],
            'email': request.json['email'],
            'type': request.json['type']
        }
        snapshot = members_ref.add(payload)
        return snapshot.data(), 200
    except Exception as e:
        return f"An Error Occurred: {e}"
    
@members.route('/get', methods=['GET'])
def get():
    try:
        members_snapshot = members_ref.get()
        return members_snapshot, 200
    except Exception as e:
        return f"An Error Occurred: {e}"
    
@members.route('/get/<id>', methods=['GET'])
def get_by_id(id):
    try:
        member_snapshot = members_ref.document(id).get()
        return member_snapshot.data(), 200
    except Exception as e:
        return f"An Error Occurred: {e}"
    
@members.route('/update/<id>', methods=['PUT'])
def update(id):
    try:
        payload = {
            'name': request.json['name'],
            'roll': request.json['roll'],
            'email': request.json['email'],
            'type': request.json['type']
        }
        snapshot = members_ref.document(id).update(payload)
        return snapshot.data(), 200
    except Exception as e:
        return f"An Error Occurred: {e}"
    
@members.route('/delete/<id>', methods=['DELETE'])
def delete(id):
    try:
        members_ref.document(id).delete()
        return "Deleted", 200
    except Exception as e:
        return f"An Error Occurred: {e}"
    