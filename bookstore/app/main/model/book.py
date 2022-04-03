from .. import db


class Book(db.Model):
    """Book model for storing related data"""
    __tablename__ = "book"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(255), unique=False, nullable=False)
    genre = db.Column(db.String(255), unique=False, nullable=False)
    author = db.Column(db.String(255), unique=False, nullable=False)
    publish_date = db.Column(db.Date, unique=False, nullable=False)
    price = db.Column(db.Float, unique=False, nullable=False)
    # make the relationship (Book-Publisher) bidirectinal
    # Many to One
    publisher_id = db.Column(db.Integer, db.ForeignKey('publisher.id'))
    publisher = db.relationship("Publisher", back_populates="books")
