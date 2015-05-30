from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return "Hello you are at the root level"

from socapp.modules.cat.routes import cat_routes
from socapp.modules.dog.routes import dog_routes
from socapp.modules.monkey.routes import monkey_routes


app.register_blueprint(cat_routes, url_prefix='/animal/cat')
app.register_blueprint(dog_routes, url_prefix='/animal/dog')
app.register_blueprint(monkey_routes, url_prefix='/animal/monkey')
