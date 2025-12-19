from sqlalchemy import Column, Integer, Float, String, ForeignKey
from sqlalchemy.orm import declarative_base, relationship
from db import engine

Base = declarative_base()

class Department(Base):
    __tablename__ = 'department'

    id = Column(Integer, primary_key=True)
    dept_name = Column("department", String)
    location = Column(String)

    employees = relationship("Employee", back_populates="department")



class Employee(Base):
    __tablename__ = 'employees'

    id = Column(Integer, primary_key=True)
    name = Column("emp_name", String)
    joining_date = Column("emp_date",String)

    dept_id = Column(Integer, ForeignKey('department.id'))
    department = relationship("Department", back_populates="employees")

    salaries = relationship("Salary", back_populates="employee")


class Salary(Base):
    __tablename__ = 'payroll'

    id = Column(Integer, primary_key=True)
    month = Column(Integer)
    year = Column(Integer)
    amount = Column(Float)

    emp_id = Column(Integer, ForeignKey('employees.id'))
    employee = relationship("Employee", back_populates="salaries")

Base.metadata.create_all(engine)