from ..config.database import db
from ..models.member import Member
from ..models.borrowing import Borrowing
from sqlalchemy import select, or_
from math import ceil


class MemberService:
    @staticmethod
    def add_member(name, email, phone, address):

        if not all([name, email, phone, address]):
            raise ValueError("All fields are required")

        if not Member.validate_email(email):
            raise ValueError("Invalid email format")

        if not Member.validate_phone(phone):
            raise ValueError("Invalid phone format")

        if Member.query.filter_by(email=email).first():
            raise ValueError("Email already exists")
        member = Member(name=name, email=email, phone=phone, address=address)
        db.session.add(member)
        db.session.commit()
        return member

    @staticmethod
    def get_member_borrowings(id, status=None, page=1, limit=10):

        member = db.session.get(Member, id)
        if not member:
            raise ValueError("Member not found")

        query = select(Borrowing).where(Borrowing.member_id == id)

        if status:
            if status.upper() not in ["BORROWED", "RETURNED"]:
                raise ValueError("Status must be either 'BORROWED' or 'RETURNED'")
            query = query.where(Borrowing.status == status.upper())

        total = db.session.scalar(select(db.func.count()).select_from(query.subquery()))

        borrowings = (
            db.session.execute(
                query.order_by(Borrowing.borrow_date.desc())
                .offset((page - 1) * limit)
                .limit(limit)
            )
            .scalars()
            .all()
        )

        return {
            "data": [
                {
                    "id": borrowing.id,
                    "borrow_date": borrowing.borrow_date.isoformat(),
                    "return_date": (
                        borrowing.return_date.isoformat()
                        if borrowing.return_date
                        else None
                    ),
                    "status": borrowing.status,
                    "book": {
                        "id": borrowing.book.id,
                        "title": borrowing.book.title,
                        "author": borrowing.book.author,
                        "isbn": borrowing.book.isbn,
                    },
                }
                for borrowing in borrowings
            ],
            "pagination": {
                "total": total,
                "page": page,
                "limit": limit,
                "totalPages": ceil(total / limit) if limit > 0 else 1,
            },
        }
