from .. import db


class Purchase(db.Model):
    """ Customer Model for storing related data info """
    __tablename__ = "purchase"

    order = None
    customer = None
    book = None
