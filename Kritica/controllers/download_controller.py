```python
from Kritica.services.download_service import DownloadService
from Kritica.utils.file_handler import download_file
from Kritica.models.book import Book
from Kritica.models.user import User

class DownloadController:
    def __init__(self):
        self.download_service = DownloadService()

    def handle_download(self, user_id, book_id):
        user = User.get(user_id)
        book = Book.get(book_id)

        if not user or not book:
            return {"message": "User or Book not found"}

        if book.approval_status != 'approved':
            return {"message": "Book not approved yet"}

        file_path = self.download_service.download_book(book_id)

        if not file_path:
            return {"message": "Download error"}

        download_file(file_path)

        return {"message": "Download success"}
```