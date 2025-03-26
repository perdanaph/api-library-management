from ..config.database import db
from ..models.member import Member


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
