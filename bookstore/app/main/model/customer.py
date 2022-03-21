from .. import db


class Customer(db.Model):
    """ Customer Model for storing related data info """
    __tablename__ = "customer"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    email = db.Column(db.String(255), unique=True, nullable=False)
    name = db.Column(db.String(255), nullable=False)
    phone_number = db.Column(db.Integer, unique=True, nullable=False)