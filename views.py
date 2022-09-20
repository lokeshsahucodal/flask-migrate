from models import CarsModel
from app import db, app
from flask import request, views, send_from_directory
import datetime
import os


class MediaView(views.MethodView):

    def get(self, filename):
        return send_from_directory(app.config['UPLOAD_FOLDER'], filename, as_attachment=True)


class CarsView(views.MethodView):

    def get(self, car_id=None):
        if car_id:
            car = CarsModel.query.get_or_404(car_id)
            response = {
                "id": car.id,
                "name": car.name,
                "model": car.model,
                "doors": car.doors,
                "image": car.image,
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
                    "image": car.image,
                    "created_at": car.created_at,
                    "updated_at": car.updated_at
                } for car in cars]

        return {"count": len(results), "cars": results}

    def post(self):
        name = request.form.get('name')
        if CarsModel.query.filter_by(name=name).first():
            return {"message": f"car {name} Already Exists."}
        image_name = None
        if 'image' in request.files and request.files['image']:
            image = request.files['image']
            image.save(os.path.join(app.config['UPLOAD_FOLDER'], image.filename))
            image_name = image.filename
        new_car = CarsModel(name=name, model=request.form.get('model'), doors=request.form.get('doors'), image=image_name)
        db.session.add(new_car)
        db.session.commit()
        return {"message": f"car {new_car.name} has been created successfully."}

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
        if 'image' in request.files and request.files['image']:
            image = request.files['image']
            image.save(os.path.join(app.config['UPLOAD_FOLDER'], image.filename))
            car.image = image.filename
        db.session.add(car)
        db.session.commit()
        return {"message": f"car {car.name} successfully updated"}
