from flask import request
from werkzeug.security import generate_password_hash
def register_user():
  '''Gathers data to register the new user with'''
  new_user_data = {
    "username": request.form.get('register_username'),
    "password_hash": generate_password_hash(request.form.get('register_password')),
    "email": request.form.get('register_email')
  }
  return new_user_data
