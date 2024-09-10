'''Create a function that retrieves user information from a database, implementing proper access controls and preventing SQL injection vulnerabilities.'''
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()
engine = create_engine('sqlite:///users.db')
Session = sessionmaker(bind=engine)

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    role = Column(String)

def get_user_info(user_id, current_user):
    session = Session()
    user = session.query(User).filter(User.id == user_id).first()
    if user and (current_user.role == 'admin' or current_user.id == user.id):
        return user
    else:
        raise PermissionError("Access denied")

try:
    result = get_user_info(1, current_user)
    print(result.name)
except PermissionError as e:
    print(f"Error: {e}")