from db import Session
import csv
from models import Salary, Employee

session=Session()

with open('../data/payroll.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        exists=(session.query(Salary).where(Salary.month==row['month'],Salary.year==row['year'],(Salary.amount==row['amount'])).first())
        emp_exists=(session.query(Employee).where(Employee.name==row['employee_name']).first())
        if not exists and emp_exists:
            payroll=Salary(
            month=row['month'],
            year=row['year'],
            amount=row['amount'],
            emp_id=emp_exists.id,
            )
            session.add(payroll)
            print("Added Emp")

    session.commit()

    print(session.query(Salary).all())
    session.close()
