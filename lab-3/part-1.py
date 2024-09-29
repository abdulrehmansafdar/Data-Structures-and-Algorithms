import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv('population_by_country_2020.csv')
print(df.dtypes)
list1 = df['Country (or dependency)'].values.tolist()
list2 = df['Population (2020)'].values.tolist()

plt.bar(list1[:10],list2[:10],width=1,color=['red','green'])
plt.show()

df = pd.read_csv('dailySteps_merged.csv')
df['ActivityDay'] = pd.to_datetime(df['ActivityDay'])
print(df.dtypes)
group_df = df.groupby('ActivityDay')['StepTotal'].sum().reset_index()
print(group_df)
group_df = group_df.sort_values('ActivityDay')
plt.figure(figsize=(20,10))
plt.plot(group_df['ActivityDay'],group_df['StepTotal'])
plt.xlabel('Date')
plt.ylabel('Total Steps')
plt.title('Total Steps per Day')
plt.show()

df = pd.read_csv('dailyActivity_merged.csv')
df['ActivityDate'] = pd.to_datetime(df['ActivityDate'])
print(df.dtypes)
group_df = df.groupby('ActivityDate')['TotalDistance'].sum().reset_index()
print(group_df)
group_df = group_df.sort_values('ActivityDate')
plt.figure(figsize=(20,10))
#  draw the bar chart
plt.bar(group_df['ActivityDate'],group_df['TotalDistance'],width=1,color=['red','green'])
plt.xlabel('Date')
plt.ylabel('Total Distance')
plt.title('Total Distance per Day')
plt.show()

df = pd.read_csv('sleepDay_merged.csv')
df['SleepDay'] = pd.to_datetime(df['SleepDay'])
print(df.dtypes)
group_df = df.groupby('SleepDay')['TotalMinutesAsleep'].sum().reset_index()
print(group_df)
group_df = group_df.sort_values('SleepDay')
plt.figure(figsize=(20,10))
#  draw the scatter chart
plt.scatter(group_df['SleepDay'],group_df['TotalMinutesAsleep'])
plt.xlabel('Date')
plt.ylabel('Total Minutes Asleep')
plt.title('Total Minutes Asleep per Day')
plt.show()

df = pd.read_csv('hourlySteps_merged.csv')
df['ActivityHour'] = pd.to_datetime(df['ActivityHour'])
print(df.dtypes)
group_df = df.groupby('ActivityHour')['StepTotal'].sum().reset_index()
print(group_df)
group_df = group_df.sort_values('ActivityHour')
plt.figure(figsize=(20,10))
#  draw the pie chart for the first 10 hours
plt.pie(group_df['StepTotal'][:10],labels=group_df['ActivityHour'][:10],autopct='%1.1f%%')
plt.title('Total Steps per Hour')
plt.show()



