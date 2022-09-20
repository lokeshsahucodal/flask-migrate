from views import CarsView, MediaView
from app import app


app.add_url_rule('/cars', view_func=CarsView.as_view('cars'))
app.add_url_rule('/cars/<int:car_id>/', view_func=CarsView.as_view('cars_id'))
app.add_url_rule('/media/<path:filename>', view_func=MediaView.as_view('filename'))

if __name__ == '__main__':
    app.run(debug=True)

