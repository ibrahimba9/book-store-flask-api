from .. import db


class Order(db.Model):
    """ Customer Model for storing related data info """
    __tablename__ = "order"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    order_date = db.Column(db.Date, unique=False, nullable=False)
    total_price = db.Column(db.Float, unique=False, nullable=False)
