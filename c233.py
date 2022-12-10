import pandas as pd 
from keras.model import Sequential
from keras.layers import Dense 

df = pd.read_csv('projectC233_studentData.csv', delimetwr=',')

df['Total_marks_obtained']=df.iloc[:,['#Add_all_3_subject_columns_here']]

df.loc[df['Add Column here'] > 250, 'Add Grade column here'] = 'A'
df.loc[df['Add Column here'] < 250, 'Add Grade column here'] = 'B'