```python
from flask import Blueprint, render_template, request, redirect, url_for, flash
from Kritica.models.book import Book
from Kritica.services.download_service import download_book
from Kritica.utils.file_handler import download_file

download_view = Blueprint('download_view', __name__)

@download_view.route('/download', methods=['GET'])
def download_form():
    books = Book.query.filter_by(approval_status='approved').all()
    return render_template('download.html', books=books)

@download_view.route('/download', methods=['POST'])
def handle_download():
    book_id = request.form.get('book_id')
    book = Book.query.get(book_id)
    if book:
        file_path = download_book(book)
        if file_path:
            return download_file(file_path)
        else:
            flash('Download error', 'download_error')
            return redirect(url_for('download_form'))
    else:
        flash('Book not found', 'download_error')
        return redirect(url_for('download_form'))
```