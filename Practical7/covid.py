import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

os.chdir("D:\下载")
#os.getcwd()
#os.listdir()

covid_data = pd.read_csv("full_data.csv")
#covid_data.head(5)
#covid_data.info()

#covid_data.describe()  #fanwei
covid_data.iloc[0,1]

covid_data.iloc[9:20,0:5]

judge_Afghanistan = []
for i in range(len(covid_data)):
    if covid_data.iloc[i,1] == "Afghanistan":
        judge_Afghanistan.append(True)
    else:
        judge_Afghanistan.append(False)
print(covid_data.loc[judge_Afghanistan,"total_cases"])
#covid_data.loc[2:4,"date"]

judge_China = []
for i in range(len(covid_data)):
    if covid_data.iloc[i,1] == "China":
        judge_China.append(True)
    else:
        judge_China.append(False)
China_new_data = covid_data.iloc[judge_China,[0,2,3]]
China_dates = China_new_data.iloc[:,0]
China_new_cases = China_new_data.iloc[:,1]
China_new_deaths = China_new_data.iloc[:,2]
print(f'The mean of the China_new_cases is {np.mean(China_new_cases)}\nThe mean of the China_new_deaths is {np.mean(China_new_deaths)}')

plt.boxplot(China_new_cases,showfliers=False,labels=['China new cases'])
plt.title('Boxplot of China new cases')

plt.plot(China_dates, China_new_cases, 'b+')

plt.xticks(China_dates.iloc[0:len(China_dates):4],rotation=-90)

#question  Are there places in the World where there have not yet been more than 10 total infections(as of 31 March)? If so, where are they?

date=[]
for y in range(len(covid_data)):
    if covid_data.iloc[y,0] == "2020-03-31":
        date.append(True)
    else:
        date.append(False)
list_f=covid_data.iloc[date,[1,4]]
sum=[]
for w in range(len(list_f)):
    if int(list_f.iloc[w,1])<=10:
        sum.append(True)
    else:
        sum.append(False)
list_f.iloc[sum,0]
list_g=list_f.iloc[sum,0]
print(list_g)