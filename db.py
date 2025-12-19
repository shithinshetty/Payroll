from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///payroll_analytics.db',echo=False)

Session = sessionmaker(bind=engine)


