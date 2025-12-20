from sqlalchemy import func
from db import Session
from models import Department, Employee,Salary

session = Session()
result = (
    session.query(
        Department.dept_name,
        func.sum(Salary.amount).label("salary")
    )
    .join(Employee, Employee.dept_id == Department.id)
    .join(Salary, Salary.emp_id == Employee.id)
    .group_by(Department.dept_name)
    .all()
)

for dept, salary in result:
    print(dept, salary)

session.close()
