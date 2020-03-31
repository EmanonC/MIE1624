from bs4 import BeautifulSoup
from sql.sql_tool import sql_helper
import time
import requests

def soup_content(soup):
    html = soup.content
    return BeautifulSoup(html, 'html.parser')
helper=sql_helper()

# helper.add_Job_Descriptioncription(herf='1',job_name='1',company_name='1',requirements=['123','321'])

IndeedJobList=helper.get_indeed_jobs()
print(len(IndeedJobList))
