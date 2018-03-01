from flask import jsonify, request
from requests import get

def getCrimes(query):
    response = get(f"https://data.raleighnc.gov/resource/3bhm-we7a.json?{query}")

    return jsonify(response.json())