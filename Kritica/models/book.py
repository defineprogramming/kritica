```python
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from Kritica.config.database import Base

class Book(Base):
    __tablename__ = 'books'

    book_id = Column(Integer, primary_key=True)
    title = Column(String(100), nullable=False)
    author = Column(String(100), nullable=False)
    file_format = Column(String(10), nullable=False)
    file_path = Column(String(200), nullable=False)
    uploader_id = Column(Integer, ForeignKey('users.user_id'))
    approval_status = Column(String(20), default='Pending')

    uploader = relationship('User', back_populates='books')

    def __init__(self, title, author, file_format, file_path, uploader_id):
        self.title = title
        self.author = author
        self.file_format = file_format
        self.file_path = file_path
        self.uploader_id = uploader_id
```