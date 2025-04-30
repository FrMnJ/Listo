from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String(50), unique=True, nullable=False)
    full_name = Column(String(100), nullable=False)
    email = Column(String(100), unique=True, nullable=False)
    phone_number = Column(String(20), unique=True, nullable=True)
    address = Column(String(200), nullable=True)
    hashed_password = Column(String(255), nullable=False)
    last_login = Column(String(50), nullable=True)
    is_verified = Column(Integer, default=0)  # 0 for False, 1 for True
    language = Column(String(10), default='en')
    utm_source = Column(String(50), nullable=True)
    device_used = Column(String(50), nullable=True)
    location = Column(String(100), nullable=True)
    url_profile = Column(String(255), nullable=True)
    url_drive_license = Column(String(255), nullable=True)
    url_identification = Column(String(255), nullable=True)



