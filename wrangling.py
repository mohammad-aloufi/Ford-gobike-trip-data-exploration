#Data wrangling for the ford-fordgobike dataset
#Note that the cleaning in here is the result of a visual assessment

#import libraries
import pandas as pd

#Load dataset and print shape
df =pd.read_csv('fordgobike-tripdata-original.csv')
print(df.shape)

#Drop rows we don't need
df.drop(['start_station_id', 'start_station_latitude', 'start_station_longitude', 'end_station_id', 'end_station_latitude', 'end_station_longitude', 'bike_id'], inplace=True, axis=1)

#Drop rows with missing values
df.dropna(axis =0, how ='any', inplace =True)

#Rename the member birth year column
df.rename(columns ={'member_birth_year': 'age'}, inplace =True)

#Replace yes and no in the bike_share_for_all_trip with zeros and ones
df['bike_share_for_all_trip'].replace({'No': 0, 'Yes': 1}, inplace =True)

#Convert the birth years to age
age_list =[]
for i in range (0, len(df['age'])):
    age_list.append(2021-df.iloc[i]['age'])

df['age'] =age_list

#Convert start_time and end_time to datetime object
df['start_time'] = pd.to_datetime(df['start_time'])
df['end_time'] = pd.to_datetime(df['end_time'])

#Create new columns bassed on the start_time datetime column
df['duration_min'] = df['duration_sec']/60
df['start_date'] = df.start_time.dt.strftime('%Y-%m-%d')
df['start_hour'] = df.start_time.dt.strftime('%H')
df['start_day'] =df.start_time.dt.strftime('%A')
df['start_month'] = df.start_time.dt.strftime('%B')

#Create new columns bassed on the end_time datetime column
df['end_date'] =df.end_time.dt.strftime('%Y-%m-%d')
df['end_hour'] =df.end_time.dt.strftime('%H')
df['end_day'] =df.end_time.dt.strftime('%A')
df['end_month'] =df.end_time.dt.strftime('%B')

#now we drop the datetime columns since we created new columns
df.drop(['duration_sec', 'start_time', 'end_time'], inplace=True, axis=1)

print (df.shape)

#Change user_type
df['user_type'] = df['user_type'].astype('category')
df['member_gender'] = df['member_gender'].astype('category')
#Save cleaned dataset
print (df.dtypes)
df.to_csv('fordgobike-tripdata.csv', index =False)