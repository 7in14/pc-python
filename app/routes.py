from app import app
from flasgger import swag_from
from flask import jsonify, request
from app.controllers import crime

@app.route('/ping')
@swag_from('/app/swagger/ping.yml')
def ping():
    return "pong"

@app.route('/file')
@swag_from('/app/swagger/file.yml')
def getFile(): 
    file = open("README.md", "r")  
    return jsonify({ "readme": file.read()})

@app.route('/raleigh/crime')
@swag_from('/app/swagger/crime.yml')
def getCrimes():
    return crime.getCrimes(request.args.get('query'))
