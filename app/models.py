from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker


Base = declarative_base()


class User(Base):
    __tablename__ = 'user'
    
    iduser = Column(Integer, primary_key=True)
    username = Column(String, nullable=False, unique=True)
    password = Column(String, nullable=False)
    email = Column(String, nullable=False, unique=True)

    def __repr__(self) -> str:
        return f'<User {self.username} {self.email}>'


class DataBase:
    def __init__(self, db_name: str) -> None:
        engine = create_engine(f'sqlite:///{db_name}')
        Base.metadata.create_all(engine)
        Session = sessionmaker(engine)
        self.session = Session()
    
    def get_users(self):
        return self.session.query(User).all()

    def filter_users(self, **values):
        return self.session.query(User).filter_by(**values).all()

    def insert_user(self, user):
        self.session.add(user)
        self.session.commit()

    def update_user(self, user):
        self.session.commit()

    def delete_user(self, user):
        self.session.delete(user)
        self.session.commit()

