import pandas as pd
import asyncio
import collections

skillCounter=collections.Counter()
skillList=[]
for i in range(26):
    file=f"/Users/yilunhuang/Desktop/Arduino/NSEmu/MIE1624/Data/{chr(i+65)}.txt"
    words=pd.read_table(file,header=None)
    words=list(words[0])
    words=[str(w).lower() for w in words]
    skillList+=words

df=pd.read_csv("/Users/yilunhuang/Desktop/Arduino/NSEmu/MIE1624/job_requirement_describtion.csv",header=None)

requirementDF=df[2]

#compare_skills function matches skills from database with job requirements string
#The skills pool is too large, so we use compare_skills function to filtering data-science irrelative skills
async def compare_skills(DF,skillList):
    matchedSkill=[]
    for i in range(len(DF)):
        requirement=str(DF.iloc[i]).split(' ')
        requirement=[_.lower() for _ in requirement]
        for skill in skillList:
            if skill in requirement:
                matchedSkill.append(skill)
    return matchedSkill

num=100
tasknum=10

start=0
while start+tasknum*num<len(requirementDF):
    print(start)
    tasks = []
    for i in range(tasknum):
        start+=num
        tasks.append(compare_skills(DF=requirementDF[start:start+num],skillList=skillList))
    loop = asyncio.get_event_loop()
    results=loop.run_until_complete(asyncio.wait(tasks))
    results=results[0]
    for result in results:
        skillCounter.update(result.result())
data=[]
for i in skillCounter:
    data.append([i,skillCounter[i]])
df=pd.DataFrame(data=data,columns=['skill','count'])
df.to_csv('single_skills.csv')