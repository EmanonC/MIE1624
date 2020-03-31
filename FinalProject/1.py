import pandas as pd
import asyncio
import collections

# skillList=[]
# for i in range(26):
#     file=f"/Users/yilunhuang/Desktop/Arduino/NSEmu/MIE1624/Data/{chr(i+65)}.txt"
#     print(file)
#     words=pd.read_table(file,header=None)
#     words=list(words[0])
#     skillList+=words

df=pd.read_csv("/Users/yilunhuang/Desktop/Arduino/NSEmu/MIE1624/job_requirement_describtion.csv",header=None)

# print(df.head())
c=collections.Counter()
c.update([1,1,1,1,2,3,1,21,3,1,21,3,4,13,1,1])
print(list(c))
print(c.most_common())
print(list(c.most_common()))
for i,j in c.most_common():
    print(i,j)