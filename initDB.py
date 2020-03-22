from main import app
from models import db

# db.init_app(app)
db.create_all(app=app)