import pandas as pd
df = pd.read_csv(r"C:\Users\mijaj\python\projects\student_performance_analyzer\student_data.csv")
corr=df.select_dtypes(include=['int64','float64']).corr()
target=corr['exam_score'].sort_values(ascending=False)
print(target)