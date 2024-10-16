from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Order(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    product = db.Column(db.String(100), nullable=False)
    location = db.Column(db.String(100), nullable=False)
    customer_id = db.Column(db.String(50), nullable=False)
    delivery_date = db.Column(db.Date, nullable=False)
    warehouse_id = db.Column(db.String(50), nullable=False)

def init_db(app):
    db.init_app(app)
    with app.app_context():
        db.create_all()
