# from sqlalchemy import (Integer, Column, String)
# from sqlalchemy.ext.declarative import declarative_base
import sqlalchemy as sa

metadata = sa.MetaData()
tbl_user = sa.Table(
    'tbl_user',
    metadata,
    sa.Column('id', sa.Integer, primary_key=True, autoincrement=True),
    sa.Column('name', sa.String(255), default='')
)
# Base = declarative_base()
#
#
# class BaseModel(object):
#     # 模型基类
#     create_time = Column(Integer)
#     update_time = Column(Integer)
#
#
# class Users(Base, BaseModel):
#     # 用户类
#     __tablename__ = 'tbl_user'
#     id = Column(Integer, primary_key=True, autoincrement=True)
#     name = Column(String(255), default='')
#     __table_args__ = {
#         'mysql_charset': 'utf8mb4'
#     }
