```python
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from Kritica.config.database import Base

class Approval(Base):
    __tablename__ = 'approvals'

    approval_id = Column(Integer, primary_key=True, index=True)
    book_id = Column(Integer, ForeignKey('books.book_id'))
    approver_id = Column(Integer, ForeignKey('users.user_id'))
    status = Column(String, default='Pending')

    book = relationship('Book', back_populates='approvals')
    approver = relationship('User', back_populates='approvals')
```