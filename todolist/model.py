from sqlalchemy.engine import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, Integer, Date
from sqlalchemy.orm import sessionmaker
from datetime import datetime

engine = create_engine("sqlite:///todo.db?check_same_thread=False")
Base = declarative_base()


class Task(Base):
    __tablename__ = "task"

    id = Column(Integer, primary_key=True)
    task = Column(String, nullable=False)
    deadline = Column(Date, default=datetime.today())

    def __repr__(self):
        return self.task


Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()


def get_today_tasks():
    dt = datetime.today().date()
    return session.query(Task).filter(Task.deadline == dt).all()


def get_all_tasks():
    return session.query(Task).all()


def add_task(task, deadline):
    session.add(Task(task=task, deadline=deadline))
    session.commit()
