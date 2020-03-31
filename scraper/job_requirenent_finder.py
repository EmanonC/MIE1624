from bs4 import BeautifulSoup
from sql.sql_tool import sql_helper
import time
import requests

def soup_content(soup):
    html = soup.content
    return BeautifulSoup(html, 'html.parser')
helper=sql_helper()


IndeedJobList=helper.get_indeed_jobs()
cnt=0
tot=len(IndeedJobList)

for IndeedJob in IndeedJobList:
    #For each job found previously, go to the website and store the job informations
    url=jobHref=IndeedJob.herf
    if "https://ca.indeed.com" not in url:
        url="https://ca.indeed.com"+url
    soup = requests.get(url=url)
    soup = soup_content(soup)
    DesktopStickyContainer=soup.find('div',attrs={"class":"jobsearch-DesktopStickyContainer"})
    try:
        job_name=DesktopStickyContainer.find('div',attrs={"class":"jobsearch-JobInfoHeader-title-container"}).getText()
        company_name=DesktopStickyContainer.find('div',attrs={"class":"jobsearch-JobInfoHeader-subtitle"}).getText()
    except:
        helper.set_indeed_job_is_scrp(IndeedJob)
        cnt+=1
        continue
    JobContent=soup.find('div',attrs={"class":"jobsearch-ViewJobLayout-jobDisplay"})
    #Find the requirements
    req_list=JobContent.find_all('li')
    req_list_string=[_.getText() for _ in req_list]
    #Add job info to database
    helper.add_Job_Description(href=jobHref,job_name=job_name,company_name=company_name,requirements=req_list_string)
    helper.set_indeed_job_is_scrp(IndeedJob)
    cnt+=1
    if cnt % 10 == 9:
        try:
            print("{}%".format(str(cnt/tot*100)[:4]))
        except:
            pass
        print("sleep")
        time.sleep(5)
        print("i'm waking up")