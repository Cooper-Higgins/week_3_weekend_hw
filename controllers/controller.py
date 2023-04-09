from flask import render_template, request, redirect
from app import app
from models.library import library, add_new_book, burn_book
from models.book import *

@app.route('/library')
def index():
    return render_template("index.html", title="CodeClan Library", library=library)

@app.route('/library', methods=['POST'])
def add_book():
    id = len(library)+1
    title = request.form['title']
    author = request.form['author']
    genre = request.form['genre']
    checked_out = "checked_out" in request.form
    new_book = Book(id, title, author, genre, checked_out)
    add_new_book(new_book)
    return redirect('/library')

@app.route('/library/delete/<title>', methods=['POST'])
def burn(title):
  burn_book(title)
  return redirect('/library')

@app.route('/library/<int:id>')
def view_book(id):
    return render_template("view_book.html", title="Book Full Details", book=library[id -1])