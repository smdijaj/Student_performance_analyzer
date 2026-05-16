import pandas as pd 
df=pd.read_csv(r'C:\Users\mijaj\python\projects\student_performance_analyzer\student_data.csv')
print(df.head())
print("rows:",len(df))
print("columns:")
print(df.columns.tolist())