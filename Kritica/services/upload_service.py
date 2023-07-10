```python
from Kritica.models.user import User
from Kritica.models.book import Book
from Kritica.utils.file_handler import upload_file
from Kritica.utils.validator import validate_book
from Kritica.config.database import db_session

class UploadService:
    @staticmethod
    def upload_book(user_id, title, author, file_format, file):
        user = User.query.get(user_id)
        if not user:
            raise Exception("User not found")

        if not validate_book(title, author, file_format):
            raise Exception("Invalid book data")

        file_path = upload_file(file)

        new_book = Book(title=title, author=author, file_format=file_format, file_path=file_path, uploader_id=user_id, approval_status='Pending')
        db_session.add(new_book)
        db_session.commit()

        return new_book
```