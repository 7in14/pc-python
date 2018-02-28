from app import app
from flasgger import swag_from
from flask import jsonify

@app.route('/ping')
@swag_from('/app/swagger/ping.yml')
def ping():
    return "pong"

@app.route('/file')
@swag_from('/app/swagger/file.yml')
def file(): 
    file = open("README.md", "r")  
    return jsonify({ "readme": file.read()})