```python
from Kritica.models.user import User
from Kritica.models.book import Book
from Kritica.models.approval import Approval

def validate_user(user):
    if not isinstance(user, User):
        raise ValueError("Invalid user object")
    if not user.user_id or not user.username or not user.password or not user.email:
        raise ValueError("Missing user information")

def validate_book(book):
    if not isinstance(book, Book):
        raise ValueError("Invalid book object")
    if not book.book_id or not book.title or not book.author or not book.file_format or not book.file_path or not book.uploader_id:
        raise ValueError("Missing book information")

def validate_approval(approval):
    if not isinstance(approval, Approval):
        raise ValueError("Invalid approval object")
    if not approval.approval_id or not approval.book_id or not approval.approver_id:
        raise ValueError("Missing approval information")
```