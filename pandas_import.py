import numpy as np
import pandas as pd
import datetime as dt

#import data
activity = pd.read_csv('./smallData/activity_small.csv')
basal = pd.read_csv('./smallData/basal_small.csv')
bolus = pd.read_csv('./smallData/bolus_small.csv')
cgm = pd.read_csv('./smallData/cgm_small.csv')
hr = pd.read_csv('./smallData/hr_small.csv')
meal = pd.read_csv('./smallData/meal_small.csv')
smbg = pd.read_csv('./smallData/smbg_small.csv')

#drop unnamed columns
basal = basal.loc[:, ~basal.columns.str.contains('^Unnamed')]
meal = meal.loc[:, ~meal.columns.str.contains('^Unnamed')]

#Convert the “time” column to be of type “datetime” and set the indexes to be 'time'
activity['time']= pd.to_datetime(activity['time'])
basal['time']= pd.to_datetime(basal['time'])
bolus['time']= pd.to_datetime(bolus['time'])
cgm['time']= pd.to_datetime(cgm['time'])
hr['time']= pd.to_datetime(hr['time'])
meal['time']= pd.to_datetime(meal['time'])
smbg['time']= pd.to_datetime(smbg['time'])

#activity.set_index("time", inplace=True)
basal.set_index("time", inplace=True)
bolus.set_index("time", inplace=True)
cgm.set_index("time", inplace=True)
hr.set_index("time", inplace=True)
meal.set_index("time", inplace=True)
smbg.set_index("time", inplace=True)

#2B: Check the format type of each “value” column. If it is not of type “ float64 ”
#convert it by setting DataFrame.astype(float)
#check type: ---print(smbg.value.dtype)
#check for nan: ---print(activity.isnull().values.any())
activity.value.fillna('0', inplace=True)
activity.set_index("value", inplace=True)
activity.drop('###', axis=0, inplace=True)
activity.drop('0+C4218', axis=0, inplace=True)
activity.reset_index(inplace=True)
activity.set_index("time", inplace=True)
activity.value = activity.value.astype(float)
#check for unique elements: ---uniq = activity.value[~activity.value.str.isnumeric()].unique()
#print(uniq)

cgm.value = cgm.value.astype(float)
hr.value = hr.value.astype(float)
meal.value = meal.value.astype(float)

#2C: Change the “value” column name to correspond to the file name
activity.rename(columns={"value":"activity"}, inplace=True)
basal.rename(columns={"value":"basal"}, inplace=True)
bolus.rename(columns={"value":"bolus"}, inplace=True)
cgm.rename(columns={"value":"cgm"}, inplace=True)
hr.rename(columns={"value":"hr"}, inplace=True)
meal.rename(columns={"value":"meal"}, inplace=True)
smbg.rename(columns={"value":"smbg"}, inplace=True)

#3 & 4
listOfFrames = [activity, basal, bolus, hr, meal, smbg]
joinFrame = cgm.join(listOfFrames)
joinFrame.fillna(0, inplace=True) #not sure if instructions mean '0', but 0 \
#(without quotes) makes more sense
#print(joinFrame)

#5 - working with time stamps
joinFrame.index = pd.to_datetime(joinFrame.index)
#add a new column -> round to 5 min
joinFrame.insert(len(joinFrame.columns), 'time5', joinFrame.index.round('5min'))
#add a new column -> round to 15 min
joinFrame.insert(len(joinFrame.columns), 'time15', joinFrame.index.round('15min'))
#print(joinFrame)

#6
#lets group by our new times, and get the means
time5 = joinFrame.set_index("time5")
time5.drop(['Id_x', 'patient_x', 'id', 'Id_y', 'patient_y', 'time15'], axis=1, inplace=True)

time15 = joinFrame.set_index("time15")
time15.drop(['Id_x', 'patient_x', 'id', 'Id_y', 'patient_y', 'time5'], axis=1, inplace=True)

time15.to_csv('time15', sep='\t')
time5.to_csv('time5', sep='\t')



#min15 = joinFrame.groupby(['time15', 'activity', 'bolus', 'meal']).mean()
#min15.drop(['Id_x', 'patient_x', 'id', 'Id_y', 'patient_y'], axis=1, inplace=True)
#print(min15.cgm.mean())
#min15 = joinFrame.groupby('time15')[['activity', 'bolus', 'meal']].mean()
#print(min15)





#print(activity)
#print(basal)
#print(bolus)
#print(cgm)
#print(hr)
#print(meal)
#print(smbg)
