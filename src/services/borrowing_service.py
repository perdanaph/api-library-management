from ..models.borrowing import Borrowing
from ..models.book import Book
from ..models.member import Member
from ..config.database import db
from datetime import date
from sqlalchemy.exc import SQLAlchemyError


class BorrowingService:
    @staticmethod
    def borrow_book(book_id, member_id):
        try:
            book = Book.query.with_for_update().get(book_id)
            if not book:
                raise ValueError("Book not Found")
            if book.stock <= 0:
                raise ValueError("Book out of stock")

            member = Member.query.get(member_id)
            if not member:
                raise ValueError("Member not Found")

            current_borrowing_book = Borrowing.query.filter_by(
                member_id=member_id, status="BORROWED"
            ).count()

            if current_borrowing_book >= 3:
                raise ValueError("Member has reached maximum borrowing limit (3 books)")

            book.stock -= 1

            borrowing = Borrowing(
                book_id=book_id,
                member_id=member_id,
                borrow_date=date.today(),
                status="BORROWED",
            )

            db.session.add(borrowing)
            db.session.commit()

            return borrowing
        except SQLAlchemyError as e:
            db.session.rollback()
            raise ValueError(f"Database error: {str(e)}")
        except ValueError as e:
            db.session.rollback()
            raise
        except Exception as e:
            db.session.rollback()
            raise ValueError(f"Unexpected error: {str(e)}")

    @staticmethod
    def return_book(borrowing_id):
        try:
            db.session.begin()
            borrowing = Borrowing.query.with_for_update().get(borrowing_id)
            print(borrowing)
            if not borrowing:
                raise ValueError("Borrowing record not found")

            if borrowing.status == "RETURNED" or borrowing.return_date != None:
                raise ValueError("Book already returned")

            book = Book.query.with_for_update().get(borrowing.book_id)
            book.stock += 1

            borrowing.status = "RETURNED"
            borrowing.return_date = date.today()

            db.session.commit()
            return borrowing

        except SQLAlchemyError as e:
            db.session.rollback()
            raise ValueError(f"Database error: {str(e)}")
        except ValueError as e:
            db.session.rollback()
            raise
        except Exception as e:
            db.session.rollback()
            print(e)
            raise ValueError(f"Unexpected error: {str(e)}")
