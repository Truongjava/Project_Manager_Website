# from fastapi import FastAPI
# from app.api.user_router import router as user_router
# from app.db.database import Base, engine

# # Initialize database tables
# Base.metadata.create_all(bind=engine)

# # Create FastAPI app
# app = FastAPI()

# # Include routers
# app.include_router(user_router)



from fastapi import FastAPI
from app.api import user_router, project_router
from app.db.database import engine
from app.models import user, project  # Thêm import cho models

# Khởi tạo ứng dụng FastAPI
app = FastAPI()

# Tạo bảng trong cơ sở dữ liệu
user.Base.metadata.create_all(bind=engine)
project.Base.metadata.create_all(bind=engine)

# Đăng ký router
app.include_router(user_router.router)
app.include_router(project_router.router)
