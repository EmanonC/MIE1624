import pandas as pd
import asyncio

# skillList=[]
# for i in range(26):
#     file=f"/Users/yilunhuang/Desktop/Arduino/NSEmu/MIE1624/Data/{chr(i+65)}.txt"
#     print(file)
#     words=pd.read_table(file,header=None)
#     words=list(words[0])
#     skillList+=words

df=pd.read_csv("/Users/yilunhuang/Desktop/Arduino/NSEmu/MIE1624/job_requirement_describtion.csv",header=None)

print(df.head())