from sqlalchemy import Column, Table
from sqlalchemy.sql.sqltypes import Integer, String

from config.db import meta

students = Table(
    'student',meta,
    Column('id',Integer,primary_key=True),
    Column('name',String(255)),
    Column('email',String(255)),
    Column('age',Integer),
    Column('country',String(255))
)