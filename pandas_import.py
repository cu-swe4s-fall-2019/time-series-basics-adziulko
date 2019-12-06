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

activity.set_index("time", inplace=True)
basal.set_index("time", inplace=True)
bolus.set_index("time", inplace=True)
cgm.set_index("time", inplace=True)
hr.set_index("time", inplace=True)
meal.set_index("time", inplace=True)
smbg.set_index("time", inplace=True)

#Check the format type of each “value” column. If it is not of type “ float64 ”
#convert it by setting DataFrame.astype(float)
#check type: ---print(smbg.value.dtype)
#check for nan: ---print(activity.isnull().values.any())
activity.value.fillna('0', inplace=True)
activity.value.replace('###','0',inplace=True)
activity.value.replace('0+C4218','0',inplace=True)
activity.value = activity.value.astype(float)
#check for unique elements: ---uniq = activity.value[~activity.value.str.isnumeric()].unique()
#print(uniq)

cgm.value = cgm.value.astype(float)
hr.value = hr.value.astype(float)
meal.value = meal.value.astype(float)





#print(activity)
#print(basal)
#print(bolus)
#print(cgm)
#print(hr)
#print(meal)
#print(smbg)
