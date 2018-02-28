from app import app
from flasgger import swag_from

@app.route('/ping')
@swag_from('/app/swagger/ping.yml')
def index():
    return "pong"
