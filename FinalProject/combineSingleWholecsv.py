import pandas as pd

dfS=pd.read_csv('/Users/yilunhuang/Desktop/Arduino/NSEmu/MIE1624/FinalProject/single_skills.csv',header=None)
dfW=pd.read_csv('/Users/yilunhuang/Desktop/Arduino/NSEmu/MIE1624/FinalProject/whole_skills.csv',header=None)

data=[]

for i in range(len(dfS)):
    data.append([dfS.iloc[i][1],dfS.iloc[i][2]])

for i in range(len(dfW)):
    if ' ' in str(dfW.iloc[i][1]):
        data.append([dfW.iloc[i][1],dfW.iloc[i][2]])
df=pd.DataFrame(data=data[1:],columns=['skill','count'])
df.to_csv('skills.csv')
df.to_csv('/Users/yilunhuang/Desktop/Arduino/NSEmu/MIE1624/Data/skills.csv')