from .. import db


class Publisher(db.Model):
    """ Publisher Model for storing related data info """
    __tablename__ = "publisher"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(255), unique=True, nullable=False)
    publish_language = db.Column(db.String(255), unique=False, nullable=False)
    foundation_date = db.Column(db.Date, unique=True, nullable=False)
    organization = db.Column(db.String(255), unique=False, nullable=False)
    # make the relationship (Book-Publisher) bidirectinal
    # One to Many
    books = db.relationship("Book", back_populates="publisher")
