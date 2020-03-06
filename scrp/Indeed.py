from bs4 import BeautifulSoup
from sql.sql_tool import sql_helper
import time
import requests

def soup_content(soup):
    html = soup.content
    return BeautifulSoup(html, 'html.parser')
helper=sql_helper()
url0="https://ca.indeed.com/jobs?q=data+science&l=Toronto,+ON&start="
n=100
type="data science"


for i in range(n):
    url=url0+"{}".format(i*10)
    soup = requests.get(url=url)
    soup = soup_content(soup)
    job_list=soup.find_all("div",attrs={"class":"jobsearch-SerpJobCard"})
    for job in job_list:
        title_class=job.find('div',attrs={"class":"title"})
        href=title_class.find('a')['href']
        helper.add_Indeed_Job_herf(herf=href,job_type=type)
    print(i)
    time.sleep(1)