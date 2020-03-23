import json
from flask_cors import CORS
from flask import Flask, request, render_template, redirect
from sqlalchemy.exc import IntegrityError
from form import myForm
from models import Log, db
from time import sleep
''' Begin boilerplate code '''


def create_app():
    app = Flask(__name__, static_url_path='')
    CORS(app)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
    app.config['SECRET_KEY'] = "MYSECRET"
    db.init_app(app)
    return app


app = create_app()

app.app_context().push()
''' End Boilerplate Code '''


@app.route('/')
def index():
    return 'Hello World!'


@app.route('/app')
def client_app():
    form = myForm()

    return app.send_static_file('app.html')


@app.route('/logs', methods=['POST', 'GET'])
def func():

    if request.method == 'POST':
        data = request.form
        log = Log(stream=int(data['stream']), id=int(data['id']))
        try:
            db.session.add(log)
            db.session.commit()
        except ValueError:
            return "ID must be an  integer"
        except IntegrityError:
            return ("ID already exist")

        return "created", 201
    else:
        data = Log.query.order_by(Log.timestamp).all()
        logs = [log.toDict() for log in data]
        return json.dumps(logs)


@app.route('/logs/<pid>', methods=['PUT'])
def func2(pid):
    data = int(request.data)
    user = Log.query.filter_by(id=pid).first()
    print(user)
    user.stream = data
    db.session.add(user)
    db.session.commit()

    return "updated", 201


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
