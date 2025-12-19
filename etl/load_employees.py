from db import  Session
from models import Employee,Department
from csv import DictReader


session =Session()

with open('../data/employees.csv') as csvfile:
    employees = DictReader(csvfile)
    for row in employees:
        exists=(session.query(Employee).where(Employee.name == row["name"],Employee.joining_date==row["joining_date"])).first()
        dept = session.query(Department).filter_by(
            dept_name=row["dept_name"]
        ).first()
        if not exists and dept:
            emp=Employee(
                name=row["name"],
                joining_date=row["joining_date"],
               dept_id=dept.id,
            )
            print("Employees Inserted Successfully")

            session.add(emp)
session.commit()

print(session.query(Employee).all())
session.close()

