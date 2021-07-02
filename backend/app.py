from flask import Flask, jsonify
from flask_jsonschema_validator import JSONSchemaValidator

import config
from connections.sql import db

from models import User

app = Flask(__name__)
JSONSchemaValidator(app=app, root="schemas")
app.config['SQLALCHEMY_DATABASE_URI'] = config.POSTGRES_CONNECTION
db.init_app(app)

with app.app_context():
    db.create_all()

@app.route("/")
def test_function():
    db.session.add(User(name="test"))
    db.session.commit()
    return {
        "test": str(User.query.filter_by(name='test').first().name)
    }