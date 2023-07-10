```python
from Kritica.models.approval import Approval
from Kritica.models.book import Book
from Kritica.utils.validator import validate_approval
from Kritica.config.database import db_session

class ApprovalService:
    @staticmethod
    def approve_book(approval_id, approver_id, status):
        approval = Approval.query.get(approval_id)
        if not approval:
            raise Exception("Approval not found")

        if not validate_approval(approval):
            raise Exception("Invalid approval data")

        approval.approver_id = approver_id
        approval.status = status
        db_session.commit()

    @staticmethod
    def get_approval_status(book_id):
        book = Book.query.get(book_id)
        if not book:
            raise Exception("Book not found")

        approval = Approval.query.filter_by(book_id=book.id).first()
        if not approval:
            raise Exception("Approval not found")

        return approval.status
```