from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import os
app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://postgres:root@localhost:5432/cars_api"
app.config['UPLOAD_FOLDER'] = os.path.join(app.root_path, 'media')

db = SQLAlchemy(app)
migrate = Migrate(app, db)



