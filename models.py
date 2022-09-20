from app import db
import datetime


class CarsModel(db.Model):
    __tablename__ = 'cars'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(), unique=True)
    model = db.Column(db.String())
    doors = db.Column(db.Integer())
    image = db.Column(db.String(), nullable=True)
    created_at = db.Column(db.DateTime, default=datetime.datetime.utcnow)
    updated_at = db.Column(db.DateTime, nullable=True)

    def __init__(self, name, model, doors, image):
        self.name = name
        self.model = model
        self.doors = doors
        self.image = image

    def __repr__(self):
        return f"<Car {self.name}>"
