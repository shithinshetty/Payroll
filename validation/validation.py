

from db import Session
from sqlalchemy import func,or_
from models import Department, Employee, Salary

session = Session()

#Count of Dep,Emp,Sal
print("Departments",session.query(Department).count())
print("Employees",session.query(Employee).count())
print ("Salary",session.query(Salary).count())

#Orphan Sal:Sal without EMP

orphans = (session.query(Salary).filter(Salary.emp_id == 'None').all())

print("Orphaned Salaries:",len(orphans))

#Duplicate Employee

results= (session.query(Employee.name,
                       func.count(Employee.id).label('count'))
                      .group_by(Employee.joining_date)
                      .having(func.count(Employee.id) > 1).all())

print("Duplicate Employee:",results)

#Duplicate_Sal

results= (session.query(Employee.name,Salary.amount,func.count(Salary.id).label('count'))
          .join(Salary.employee,)
          .group_by(Salary.emp_id,Salary.year,Salary.month)
          .having(func.count(Salary.id) > 1).all()

          )

print("Duplicate Sal:",results)

#Delete Duplicate Sal


keep_ids = (
    session.query(func.min(Salary.id))
    .group_by(Salary.emp_id, Salary.month, Salary.year)
    .all()
)

keep_ids = [i[0] for i in keep_ids]

session.query(Salary)\
    .filter(~Salary.id.in_(keep_ids))\
    .delete(synchronize_session=False)


for i in results:
    print("Deleted results",i)
session.commit()

#Invalid Salary Amounts

invalid=(
    session.query(Salary).filter(Salary.amount == 'None').all())

print("Invalid Salaries:",len(invalid))

#Invalid Employe

invalid=(
    session.query(Employee).filter(or_(Employee.id == 'None', Employee.name=='None')).all())

print("Missing  Employee:",len(invalid))

session.close()