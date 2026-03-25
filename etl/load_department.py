import csv
from db import Session
from models import Department

session = Session()

with open("data/departments.csv",newline="") as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        exists=session.query(Department).filter_by(dept_name=row['dept_name']).first()

        if not exists:
            department = Department(dept_name=row['dept_name'],
            location=row['location']
            )
            session.add(department)
session.commit()


# val = session.query(Department).all()

# for i in val:
#     print(f"{i.dept_name}, {i.location}")

session.close()

import os
print("CWD:", os.getcwd())

print("Departments: Inserted")


