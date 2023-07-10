```python
from flask import request, jsonify
from Kritica.services.upload_service import upload_book
from Kritica.utils.validator import validate_book
from Kritica.models.user import User
from Kritica.models.book import Book

def handle_upload():
    if request.method == 'POST':
        user = User.query.get(request.form['user_id'])
        if not user:
            return jsonify({"message": "User not found"}), 404

        book_data = {
            "title": request.form['title'],
            "author": request.form['author'],
            "file_format": request.form['file_format'],
            "file_path": request.form['file_path'],
            "uploader_id": user.user_id
        }

        validation_errors = validate_book(book_data)
        if validation_errors:
            return jsonify({"message": "Invalid book data", "errors": validation_errors}), 400

        book = Book(**book_data)
        upload_book(book)

        return jsonify({"message": "Book uploaded successfully, waiting for approval"}), 200
```