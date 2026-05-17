import pandas as pd

df = pd.read_csv(r"C:\Users\mijaj\python\projects\student_performance_analyzer\student_data.csv")

top = df.sort_values("exam_score", ascending=False).head(20)

print(top)