import datetime
import sqlalchemy
from sqlalchemy import orm

from db_session import SqlAlchemyBase


class News(SqlAlchemyBase):
    __tablename__ = 'users'

    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, unique=True)
    login = sqlalchemy.Column(sqlalchemy.String)
    nickname = sqlalchemy.Column(sqlalchemy.String)
    status = sqlalchemy.Column(sqlalchemy.String)