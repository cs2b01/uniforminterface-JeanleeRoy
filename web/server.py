from flask import Flask,render_template, request, session, Response, redirect
from database import connector
from model import entities
import json

db = connector.Manager()
engine = db.createEngine()

app = Flask(__name__)

@app.route('/')
def index():
    return "Desarrollo Basado en Plataformas"

@app.route('/users')
def users():
    db_session = db.getSession(engine)
    users = db_session.query(entities.User)
    data = users[:]
    return Response(json.dumps(data, cls=connector.AlchemyEncoder), mimetype = 'application/json')

@app.route('/create_user', methods = ['GET'])
def create_user():
    db_session = db.getSession(engine)
    user = entities.User(code="201800000", name="Nombre", last="Apellido", password="Password")
    db_session.add(user)
    db_session.commit()
    return "User created!"

if __name__ == '__main__':
    app.secret_key = ".."
    app.run(port=8080, threaded=True, host=('0.0.0.0'))
