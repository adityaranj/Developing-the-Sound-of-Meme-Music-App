from sqlalchemy.orm import Session
from models import User
from schemas import UserCreate
from database import SessionLocal

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def create_user(db: Session, user: UserCreate):
    db_user = User(email=user.email, hashed_password=get_password_hash(user.password))
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def get_user_by_email(db: Session, email: str):
    return db.query(User).filter(User.email == email).first()

# Add other CRUD operations as needed
