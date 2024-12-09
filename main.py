from database import get_db, engine
from Entities.User import Base
from Infrastructure.UserRepository import UserRepository
from sqlalchemy.orm import Session

# Tạo bảng trong cơ sở dữ liệu (nếu chưa tồn tại)
Base.metadata.create_all(bind=engine)

def main():
    # Lấy phiên kết nối tới cơ sở dữ liệu
    db: Session = next(get_db())
    user_repo = UserRepository(db)

    # Tạo người dùng mới
    user = user_repo.create_user(email="huongchau@gmail.com", password="9399")
    print(f"User created: {user.email}")

    

if __name__ == "__main__":
    main()
