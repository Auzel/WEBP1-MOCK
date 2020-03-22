import json
from flask_cors import CORS
from flask import Flask, request, render_template, redirect
from sqlalchemy.exc import IntegrityError
from form import myForm
from models import Log, db
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
    data = request.form
    log = Log(stream=int(data['stream']), id=int(data['id']))
    db.session.add(log)
    db.session.commit()
    # print(data)

    return redirect('/app', code=302)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
