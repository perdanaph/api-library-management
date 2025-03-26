from ..config.database import db
from datetime import date, datetime
import uuid
from sqlalchemy import Enum, ForeignKey, Integer, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

class Borrowing(db.Model):
	__tablename__ = "borrowings"
	id: Mapped[str] = mapped_column(
		db.String(36), primary_key=True, default=lambda: str(uuid.uuid4())
    )
	book_id: Mapped[str] = mapped_column( db.String(36), ForeignKey('books.id'), nullable=False ) 
	member_id: Mapped[str] = mapped_column( db.String(36), ForeignKey('members.id'), nullable=False ) 
	borrow_date: Mapped[date] = mapped_column(nullable=False) 
	return_date: Mapped[date] = mapped_column(nullable=True) 
	status: Mapped[str] = mapped_column( Enum('BORROWED', 'RETURNED', name='borrowing_status'), default='BORROWED' )
	created_at: Mapped[datetime] = mapped_column( db.TIMESTAMP, server_default=db.func.current_timestamp() )
	updated_at: Mapped[datetime] = mapped_column( db.TIMESTAMP, server_default=db.func.current_timestamp(), onupdate=db.func.current_timestamp()) 
	
	book: Mapped["Book"] = relationship(back_populates="borrowings") 
	member: Mapped["Member"] = relationship(back_populates="borrowings")
	
	__table_args__ = (
        db.Index('idx_borrowing_book_id', 'book_id'),
        db.Index('idx_borrowing_member_id', 'member_id'),
        
        db.Index('idx_borrowing_status_date', 'status', 'borrow_date'),
        

        db.Index('idx_borrowing_active', 'return_date', 
                postgresql_where=(db.text("status = 'BORROWED'"))),
    )
	
	def __repr__(self): 
		return f'<Borrowing {self.id} ({self.status})>' 
	def to_dict(self): 
		return { 
			"id": self.id, 
			"book_id": self.book_id,
			"member_id": self.member_id, 
			"borrow_date": self.borrow_date.isoformat(), 
			"return_date": self.return_date.isoformat() if self.return_date else None, 
			"status": self.status, 
			"created_at": self.created_at.isoformat(), 
			"updated_at": self.updated_at.isoformat() 
		}
