import os
from dotenv import load_dotenv
from src.config.database import db, init_db
from src.models.book import Book
from src.models.member import Member
from src.models.borrowing import Borrowing
from datetime import date



load_dotenv()
# Initialize Flask app (untuk context database)
from flask import Flask
app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL', 'postgresql://postgres:postgres@localhost/library_db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize database
init_db(app)

def test_connection():
    print("Testing database connection...")
    try:
        # Simple query to check connection
        result = db.session.execute("SELECT version()")
        print("✅ Database connection successful!")
        print("PostgreSQL version:", result.fetchone()[0])
    except Exception as e:
        print("❌ Database connection failed!")
        print("Error:", e)

def test_models():
    print("\nTesting models...")
    with app.app_context():
        try:
            # Test Book model
            book = Book(
                title="Javasripct Programming",
                author="John Doe",
                published_year=2023,
                stock=5,
                isbn="1234567890112"
            )
            db.session.add(book)
            db.session.commit()
            
            
            # Test Member model
            member = Member(
                name="Hiasa",
                email="alice@mail.com",
                phone="+628123456789",
                address="123 Main St"
            )
            db.session.add(member)
            
            db.session.commit()
            print("✅ Basic model creation successful!")

            print(f"Book ID: {book.id}")
            print(f"Member ID: {member.id}")
            
            # Test Borrowing model
            borrowing = Borrowing(
                book_id=book.id,
                member_id=member.id,
                borrow_date=date.today()
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
            
            # Cleanup (optional)
            
            
        except Exception as e:
            db.session.rollback()
            print("❌ Model test failed!")
            print("Error:", e)
        finally:
            db.session.delete(borrowing)
            db.session.delete(book)
            db.session.delete(member)
            db.session.commit()

if __name__ == '__main__':
    test_connection()
    test_models()