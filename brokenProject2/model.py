from flask_sqlalchemy import sqlAlchemy

db = SqlAlchemy()

class Book(db.Model):
    id = db.Column(db.Float, primary_key=True)
    author = db.Column(db.String(100), nullable=False)
    title = db.Column(db.String(100), nullable=False)
    year = db.Column(db.Integer, nullable=False)

class Borrow(db.Model):
    id = db.Column(db.Float, primary_key=True)
    book_id = db.Column(db.Integer, db.ForeignKey('book.id'), nullable=False)
    borrower_name = db.Column(db.String(100), nullable=False)
