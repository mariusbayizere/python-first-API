from fastapi import APIRouter, status
from fastapi.exceptions import HTTPException
from typing import Optional, List
from src.Student.schema import Student, Update_Student
from src.Student.Student_data import Students

Student_router = APIRouter()


@Student_router.get("/index")
def read_root():
    return {"message": "Welcome to Student Management System"}


@Student_router.get("/students5/{student_id}")
def read_student(student_id: int):
    return Students[student_id]


@Student_router.get("/student1")
async def read_student1(a: Optional[int] = 30, b: Optional[int] = 30) -> dict:
    sum: int = a + b
    return {"message": f"{sum}"}


@Student_router.get("/students1", response_model=List[Student])
async def read_students() -> dict:
    return Students


@Student_router.post("/create-student")
def create_student(student: Student):
    Students.append(student)
    return student


@Student_router.put("/add-student", status_code=status.HTTP_201_CREATED)
def add_student(student: Student):
    Students.append(student)
    return student


@Student_router.get("/students/{id}")
async def search_student(id: int):
    for student in Students:
        if student["id"] == id:
            return student

    raise HTTPException(status_code=404, detail="Student not found")


@Student_router.get("/search_student_email/{email}", status_code=status.HTTP_200_OK)
async def search_student_email(email: str):
    for student in Students:
        if student["email"] == email:
            return student
    raise HTTPException(status_code=404, detail="Student not found")


@Student_router.patch("/update-student/{id}", status_code=status.HTTP_202_ACCEPTED)
async def update_student(id: int, student: Update_Student):
    for studentx in Students:
        if studentx["id"] == id:
            studentx["first_name"] = student.first_name
            studentx["last_name"] = student.last_name
            studentx["email"] = student.email
            studentx["faculty"] = student.faculty
            studentx["department"] = student.department
            studentx["level"] = student.level
            studentx["cgpa"] = student.cgpa

            return studentx

    raise HTTPException(status_code=404, detail="Student not found")


@Student_router.get("/getallstudents", status_code=status.HTTP_200_OK)
async def get_all_students():
    return Students
