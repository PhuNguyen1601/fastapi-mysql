from fastapi import APIRouter

from config.db import conn
from models.index import students
from schemas.index import Student

student = APIRouter()

@student.get("/")
async def index():
    return conn.execute(students.select()).fetchall()

@student.get("/{id}")
async def get_student(id:int):
    return conn.execute(students.select().where(students.c.id == id)).fetchall()

@student.post("/")
async def store(student:Student):
    res = conn.execute(students.insert().values(
        name = student.name,
        email = student.email,
        age = student.age,
        country = student.country,
        ))
    if res.is_insert:
        data = conn.execute(students.select()).fetchall()
        return {
            "Success":True,
            "data":data
        }
    else:
        return {
            "Success":True,
            "msg":"New data added failed!!!"
        }

@student.put("/{id}")
async def update_student(id:int, student:Student):
    conn.execute(students.update().values(
        name = student.name,
        email = student.email,
        password = student.password,
    ).where(students.c.id == id))
    return conn.execute(students.select()).fetchall()

@student.delete("/{id}")
async def delete_student(id:int):
    conn.execute(students.delete().where(students.c.id == id))
    return conn.execute(students.select()).fetchall()
