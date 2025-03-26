# file ini hanya untuk percobaan melakukan interaksi dengan database untuk melakukan pengecekan database terkoneksi dengan aman

from src.config.database import db, init_db
from src.models.book import Book
from src.models.member import Member
from src.models.borrowing import Borrowing
from datetime import date

from flask import Flask

app = Flask(__name__)

init_db(app)


def test_models():
    print("\nTesting models...")
    with app.app_context():
        try:
            # Test Book model
            book = Book(
                title="dart Programming",
                author="John Doe",
                published_year=2023,
                stock=5,
                isbn="123985675218",
            )
            db.session.add(book)

            # Test Member model
            member = Member(
                name="hiese",
                email="hiasa4@mail.com",
                phone="+62812346789",
                address="123 Main St",
            )
            db.session.add(member)

            db.session.commit()
            print("✅ Basic model creation successful!")

            print(f"Book ID: {book.id}")
            print(f"Member ID: {member.id}")
            borrowing = Borrowing(
                book_id=book.id, member_id=member.id, borrow_date=date.today()
            )
            db.session.add(borrowing)
            db.session.commit()
            print("✅ Relationship model creation successful!")

            # Query test
            print("\nSample data inserted:")
            print("- Book:", book.to_dict())
            print("- Member:", member.to_dict())
            print("- Borrowing:", borrowing.to_dict(include_book=True))

            print("\nRelationship verification:")
            print("- Book borrowings:", [b.id for b in book.borrowings])
            print("- Member borrowings:", [b.id for b in member.borrowings])

        except Exception as e:
            db.session.rollback()
            print("❌ Model test failed!")
            print("Error:", e)
            raise


if __name__ == "__main__":
    test_models()
