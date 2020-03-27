from sqlalchemy import Column, String, create_engine,INTEGER
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sql.models import IndeedJobTable,JobDescibtion,JobRequirementDescibtion


class sql_helper:
    def __init__(self):
        self.db=declarative_base()
        self.engine=create_engine('mysql+pymysql://root:F=mdv/dt123@localhost/MIE1624', encoding='utf-8',echo=True)
        self.DBSession = sessionmaker(bind=self.engine)
        self.db=self.DBSession()

    def add_Indeed_Job_herf(self,herf,job_type=None):
        IndeedJob=IndeedJobTable(herf=herf,job_type=job_type)
        self.db.add(IndeedJob)
        self.db.commit()

    def add_Job_Description(self,href,job_name,company_name,requirements):
        JD=JobDescibtion(href=href,job_name=job_name,company_name=company_name)
        self.db.add(JD)
        self.db.flush()
        jid=JD.id
        self.db.commit()
        for r in requirements:
            JRD=JobRequirementDescibtion(job_id=jid,requirement=r)
            self.db.add(JRD)
            self.db.commit()

    def set_indeed_job_is_scrp(self,indeed_job):
        indeed_job.is_scrp=1
        self.db.commit()

    def get_indeed_jobs(self):
        job_hrefs=self.db.query(IndeedJobTable).filter(IndeedJobTable.is_scrp==0).all()
        return job_hrefs
