from ..config.database import db, BaseModel

class Book(BaseModel):
    __tablename__ = 'books'
    
    title = db.Column(db.String(255), nullable=False)
    author = db.Column(db.String(255), nullable=False)
    published_year = db.Column(db.Integer, nullable=False)
    stock = db.Column(db.Integer, nullable=False, default=0)
    isbn = db.Column(db.String(13), unique=True, nullable=False)
    
    borrowings = db.relationship('Borrowing', backref='book', lazy=True)
    
    def to_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'author': self.author,
            'published_year': self.published_year,
            'stock': self.stock,
            'isbn': self.isbn,
            'available': self.stock > 0
        }