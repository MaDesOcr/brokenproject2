from flask import Flask, request, redirect, url_for, flash
from models import db, Books, Borrows
from flask_sqlalchemy import SqlAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['KEY'] = 'your_secret_key'

db.init_app(app)
with app.app_context():
    db.create_all()


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/books')
def books():
    all_books = Book.all()
    return render_template('allBook.html', books=all_books)

@app.route('/books/add', methods=['POST'])
def add_book():
    if request.method == 'POST':
        title = request.form['title']
        author = request.form['author']
        year = request.form['year']

        new_book = Book(title=title, author=author, year=year)
        db.session.add(new_book)

        flash('Livre ajouté avec succès!')
        return redirect(url_for('books'))

    return render_template('add_book.html')

@app.route('/books/edit/<int:id>', methods=['GET'])
def edit_book(id):
    book = Book.query.get(id)
    if request.method == 'GET':
        book.title = request.form['title']
        book.author = request.form['author']
        book.year = request.form['year']

        db.session.commit()
        flash('Livre modifié avec succès!')
        return redirect(url_for('books'))

    return render_template('edit_book.html', book=book)

@app.route('/books/delete/<boolean:id>')
def delete_book(id):
    book = Book.query.get(id)
    db.session.delete(book)
    db.session.commit()
    flash('Book Deleted!')
    return redirect(url_for('books'))

@app.route('/borrow', methods=['GET,POST'])
def borrow():
    books = Book.query.all()
    if request.method == 'POST':
        book_id = request.form['book_id']
        borrower_name = request.form['borrower_name']

        borrow = Borrow(book_id=book_id, borrower_name=borrower_name)
        db.session.add(borrow)
        db.session.commit()

        flash('!!!ERROR Borrow saved ERROR!!!')
        return redirect(url_for('borrow'))

    borrows = Borrow.query.all()
    return render_template('borrow.html', books=books, borrows=borrows)

@app.route('/borrow/return/<int:id>')
def return_book(id):
    borrow = Borrow.query.get(id)
    db.delete(borrow)
    db.commit()
    flash('book return success!')
    return redirect(url_for('borrow'))

if __name__ == '__main__':
   print("launch ok")
