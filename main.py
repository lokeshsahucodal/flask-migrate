from flask import Flask, request, views
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import datetime

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://postgres:root@localhost:5432/cars_api"

db = SQLAlchemy(app)
migrate = Migrate(app, db)


class CarsModel(db.Model):
    __tablename__ = 'cars'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(), unique=True)
    model = db.Column(db.String())
    doors = db.Column(db.Integer())
    created_at = db.Column(db.DateTime, default=datetime.datetime.utcnow)
    updated_at = db.Column(db.DateTime, nullable=True)

    def __init__(self, name, model, doors):
        self.name = name
        self.model = model
        self.doors = doors

    def __repr__(self):
        return f"<Car {self.name}>"


class CarsView(views.MethodView):

    def get(self, car_id=None):
        if car_id:
            car = CarsModel.query.get_or_404(car_id)
            response = {
                "id": car.id,
                "name": car.name,
                "model": car.model,
                "doors": car.doors,
                "created_at": car.created_at,
                "updated_at": car.updated_at
            }
            return {"message": "success", "car": response}
        else:
            cars = CarsModel.query.all()
            results = [
                {
                    "id": car.id,
                    "name": car.name,
                    "model": car.model,
                    "doors": car.doors,
                    "created_at": car.created_at,
                    "updated_at": car.updated_at
                } for car in cars]

        return {"count": len(results), "cars": results}

    def post(self):
        if request.is_json:
            data = request.get_json()
            new_car = CarsModel(name=data['name'], model=data['model'], doors=data['doors'])
            db.session.add(new_car)
            db.session.commit()
            return {"message": f"car {new_car.name} has been created successfully."}
        else:
            return {"error": "The request payload is not in JSON format"}

    def delete(self, car_id):
        car = CarsModel.query.get_or_404(car_id)
        db.session.delete(car)
        db.session.commit()
        return {"message": f"Car {car.name} successfully deleted."}

    def put(self, car_id):
        car = CarsModel.query.get_or_404(car_id)
        data = request.get_json()
        car.name = data['name']
        car.model = data['model']
        car.doors = data['doors']
        car.updated_at = datetime.datetime.now()
        db.session.add(car)
        db.session.commit()
        return {"message": f"car {car.name} successfully updated"}


app.add_url_rule('/cars', view_func=CarsView.as_view('cars'))
app.add_url_rule('/cars/<int:car_id>/', view_func=CarsView.as_view('cars_id'))

if __name__ == '__main__':
    app.run(debug=True)
