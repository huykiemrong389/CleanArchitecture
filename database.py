from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Thay URL dưới đây theo loại cơ sở dữ liệu bạn muốn sử dụng
DATABASE_URL = "sqlite:///./app.db"  # SQLite

engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False} if "sqlite" in DATABASE_URL else {})

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_db():
    """Lấy phiên kết nối tới cơ sở dữ liệu."""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
