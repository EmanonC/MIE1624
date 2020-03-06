from sqlalchemy import Column, String, create_engine,INTEGER,TEXT
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import ForeignKey


Base = declarative_base()

class IndeedJobTable(Base):
    __tablename__ = 'indeed_job_href'
    id = Column(INTEGER, primary_key=True,autoincrement=True)
    herf=Column(TEXT)
    job_type=Column(String(127))
    is_scrp=Column(INTEGER,default=0)

class JobDescibtion(Base):
    __tablename__ = 'job_describtion'
    id = Column(INTEGER, primary_key=True, autoincrement=True)
    href = Column(TEXT)
    job_name = Column(String(127))
    company_name = Column(String(127))

class JobRequirementDescibtion(Base):
    __tablename__ = 'job_requirement_describtion'
    id = Column(INTEGER, primary_key=True, autoincrement=True)
    job_id=Column(INTEGER)
    requirement=Column(TEXT)

if __name__ == '__main__':

    engine=create_engine('mysql+pymysql://root:password@localhost/MIE1624', encoding='utf-8',echo=True)
    DBSession = sessionmaker(bind=engine)
    Base.metadata.create_all(engine)