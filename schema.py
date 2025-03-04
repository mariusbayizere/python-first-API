from pydantic import BaseModel


class Student(BaseModel):
    """
    Represents a student with various attributes.

    Attributes:
        id (int): The unique identifier for the student.
        first_name (str): The first name of the student.
        last_name (str): The last name of the student.
        email (str): The email address of the student.
        faculty (str): The faculty to which the student belongs.
        department (str): The department to which the student belongs.
        level (int): The academic level of the student.
        cgpa (float): The cumulative grade point average of the student.
    """

    id: int
    first_name: str
    last_name: str
    email: str
    faculty: str
    department: str
    level: int
    cgpa: float


class Update_Student(BaseModel):
    """
    Update_Student is a Pydantic model representing the schema for updating student information.

    Attributes:
        first_name (str): The first name of the student.
        last_name (str): The last name of the student.
        email (str): The email address of the student.
        faculty (str): The faculty to which the student belongs.
        department (str): The department to which the student belongs.
        level (int): The academic level of the student.
        cgpa (float): The cumulative grade point average of the student.
    """

    first_name: str
    last_name: str
    email: str
    faculty: str
    department: str
    level: int
    cgpa: float
