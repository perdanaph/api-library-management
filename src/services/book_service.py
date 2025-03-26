from ..models.book import Book
from ..config.database import db
from math import ceil

class BookService:
	@staticmethod
	def get_all_books(title=None, author=None, page=1, limit=10):
		query = Book.query
		if title:
			query = query.filter(Book.title.ilike(f'%{title}%'))
		if author:
			query = query.filter(Book.author.ilike(f'%{author}%'))
		total = query.count()
		books = query.offset((page - 1) * limit).limit(limit).all()
		total_pages = ceil(total/limit) if limit > 0 else 1 
		return {
			'data': [book.to_dict() for book in books],
			'pagination': {
				'total': total,
				'page': page,
				'limit': limit,
				'totalPages': total_pages
            }
        }