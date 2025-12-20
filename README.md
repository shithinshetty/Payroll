# Project Title

Employee Payroll and Analytics System

# Project Overview

This project is a mini data engineering system
that models an employee payroll workflow
It inclines schema design ,idempotent ETL pipelines, Data Validation.



# Tech Stack
Python,SQLAlchemy ORM, and Sqlite

# ETL Flow

ETL execution order:
1. Load departments
2. Load employees (validated against departments)
3. Load salary payments (validated against employees)

Each ETL step includes:
- Schema validation
- Idempotency checks to prevent duplicate inserts

# Data Validation and Idempotency

Validation:
- Skips records with missing or invalid fields
- Ensures foreign key references exist
- Validates salary amounts and date fields

Idempotency:
- Checks for existing records before insert
- Enforced with both ORM-level checks and database-level constraints

# How to Run the project

1. Create virtual environment and install dependencies
 - > python -m venv (env name)

2. Go to (env name->Scripts->Activate.ps1->copy path)
3. Run the path 
- > eg: C:\Users\XXXX\PycharmProjects\Payroll\myenv\Scripts\Activate.ps1
4. Install SQAlchemy
- >  pip install sqlalchemy
5. Configure your database path  accordingly in db.py
6. Upload your csv fils in data folder  
7. Execute ETL scripts in order
5. Run analytics/dept_payroll.py to view results and validation script to validate the entries

