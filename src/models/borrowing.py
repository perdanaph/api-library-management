from ..config.database import db, BaseModel
from datetime import datetime, date

class Borrowing(BaseModel):
    __tablename__ = 'borrowings'
    
    book_id = db.Column(db.String(36), db.ForeignKey('books.id'), nullable=False)
    member_id = db.Column(db.String(36), db.ForeignKey('members.id'), nullable=False)
    borrow_date = db.Column(db.Date, nullable=False, default=date.today)
    return_date = db.Column(db.Date)
    status = db.Column(db.Enum('BORROWED', 'RETURNED', name='borrowing_status'), default='BORROWED')
    
    def to_dict(self, include_book=False):
        data = {
            'id': self.id,
            'book_id': self.book_id,
            'member_id': self.member_id,
            'borrow_date': self.borrow_date.isoformat() if self.borrow_date else None,
            'return_date': self.return_date.isoformat() if self.return_date else None,
            'status': self.status
        }
        
        if include_book and self.book:
            data['book'] = self.book.to_dict()
            
        return data