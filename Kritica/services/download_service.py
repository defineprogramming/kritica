```python
from Kritica.models.book import Book
from Kritica.utils.file_handler import download_file
from Kritica.config.settings import download_dir

class DownloadService:
    @staticmethod
    def download_book(book_id, user_id):
        book = Book.get_book_by_id(book_id)
        if book and book.approval_status == 'approved':
            file_path = download_dir + book.file_path
            download_file(file_path, user_id)
            return True
        else:
            return False
```