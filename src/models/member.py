from ..config.database import db
from datetime import date, datetime
import uuid
from sqlalchemy import Enum, ForeignKey, Integer, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

class Member(db.Model):
	__tablename__ = "members"
	id: Mapped[str] = mapped_column(
		db.String(36), primary_key=True, default=lambda: str(uuid.uuid4())
    )
	name: Mapped[str] = mapped_column(db.String(255), nullable=False)
	email: Mapped[str] = mapped_column(db.String(255), unique=True, nullable=False)
	phone: Mapped[str] = mapped_column(db.String(15), nullable=False)
	address: Mapped[str] = mapped_column(db.Text, nullable=False)
	created_at: Mapped[datetime] = mapped_column( db.TIMESTAMP, server_default=db.func.current_timestamp() )
	updated_at: Mapped[datetime] = mapped_column( db.TIMESTAMP, server_default=db.func.current_timestamp(), onupdate=db.func.current_timestamp())
	
	borrowings: Mapped[list["Borrowing"]] = db.relationship(back_populates="member")
	__table_args__ = (
        db.Index('idx_member_email', 'email'),
        
        db.Index('idx_member_name_lower', db.func.lower('name')),
    )
	
	def __repr__(self): 
		return f'<Member {self.name} ({self.email})>' 
	def to_dict(self): 
		return { 
            "id": self.id,
            "name": self.name,
            "email": self.email,
            "phone": self.phone,
            "address": self.address,
            "created_at": self.created_at.isoformat(),
            "updated_at": self.updated_at.isoformat()
		}
