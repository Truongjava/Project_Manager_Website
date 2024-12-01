from sqlalchemy.orm import Session
from app.models.user import User
from app.schemas.user import UserCreate, UserUpdate
# from app.security import hash_password  # (Nếu bạn muốn hash mật khẩu)

# Hàm tạo người dùng
def create_user(db: Session, user: UserCreate):
    db_user = User(
        user_id=user.user_id,  # user_id do người dùng cung cấp
        username=user.username,
        email=user.email,
        role=user.role,
        full_name=user.full_name,
        profile_picture=user.profile_picture,
        password=user.password  # Mật khẩu cần được hash nếu là mật khẩu thực tế
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

# Hàm lấy người dùng theo user_id
def get_user_by_id(db: Session, user_id: str):
    return db.query(User).filter(User.user_id == user_id).first()

# Hàm lấy danh sách người dùng
def get_users(db: Session, skip: int = 0, limit: int = 10):
    return db.query(User).offset(skip).limit(limit).all()

# Hàm xóa người dùng
def delete_user(db: Session, user_id: str):
    db_user = db.query(User).filter(User.user_id == user_id).first()
    if db_user:
        db.delete(db_user)
        db.commit()
        return db_user
    return None

# Hàm cập nhật thông tin người dùng
def update_user(db: Session, user_id: str, user: UserUpdate):
    db_user = db.query(User).filter(User.user_id == user_id).first()
    if db_user:
        # Cập nhật các trường người dùng
        if user.username:
            db_user.username = user.username
        if user.email:
            db_user.email = user.email
        if user.role:
            db_user.role = user.role
        if user.full_name:
            db_user.full_name = user.full_name
        if user.profile_picture:
            db_user.profile_picture = user.profile_picture
        if user.password:
            db_user.password = user.password  # Mật khẩu có thể được hash ở đây
        db.commit()
        db.refresh(db_user)
        return db_user
    return None
