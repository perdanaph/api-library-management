from ..config.database import db
from datetime import datetime
import uuid
from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column

class Book(db.Model):
	__tablename__ = "books"
	id: Mapped[str] = mapped_column(
		db.String(36), primary_key=True, default=lambda: str(uuid.uuid4())
    )
	isbn: Mapped[str] = mapped_column( db.String(13), unique=True, nullable=False )
	title: Mapped[str] = mapped_column(db.String(255), nullable=False)
	author: Mapped[str] = mapped_column(db.String(255), nullable=False)
	published_year: Mapped[int] = mapped_column(nullable=False)
	stock: Mapped[int] = mapped_column(nullable=False, default=0)
	created_at: Mapped[datetime] = mapped_column( db.TIMESTAMP, server_default=db.func.current_timestamp() )
	updated_at: Mapped[datetime] = mapped_column( db.TIMESTAMP, server_default=db.func.current_timestamp(), onupdate=db.func.current_timestamp()) 

	borrowings: Mapped[list["Borrowing"]] = db.relationship(back_populates="book")
	
	__table_args__ = (
        db.Index('idx_book_isbn', 'isbn', unique=True),
        
        db.Index('idx_book_title_author', 'title', 'author'),
    )
	
	def __repr__(self):
		return f'<Book {self.title} (ISBN: {self.isbn})>'
	
	def to_dict(self):
		return {
            'id': self.id,
            'title': self.title,
            'author': self.author,
            'published_year': self.published_year,
            'stock': self.stock,
            'isbn': self.isbn,
            'created_at': self.created_at.isoformat() if self.created_at else None,
            'updated_at': self.updated_at.isoformat() if self.updated_at else None
        }
