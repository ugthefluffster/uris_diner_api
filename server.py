from flask import Flask
from flask_restful import Api
from flask_cors import CORS
from config import *
from db import db
from controllers import *

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = f'postgresql+psycopg2://{DB_USER}:{DB_PASS}@{DB_HOST}/postgres'
app.config['SECRET_KEY'] = '345345456456754greg45g4rb546y45tg3rtg4657y'
db.init_app(app)
api = Api(app)
CORS(app)

api.add_resource(CategoryAll, '/categories')
api.add_resource(CategoryOne, '/dishes')

@app.errorhandler(404)
def page_not_found(error):
    return {"message" : "not found"}, 404

if __name__ == '__main__':
    app.run(host='0.0.0.0')
    