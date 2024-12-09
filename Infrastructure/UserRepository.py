from sqlalchemy.orm import Session
from Entities.User import User

class UserRepository:
    def __init__(self, db: Session):
        self.db = db

    def get_user_by_email(self, email: str):
        """Tìm người dùng theo email."""
        return self.db.query(User).filter(User.email == email).first()

    def create_user(self, email: str, password: str):
        """Tạo người dùng mới."""
        new_user = User(email=email, password=password)
        self.db.add(new_user)
        self.db.commit()
        self.db.refresh(new_user)
        return new_user
