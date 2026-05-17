import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv(r"C:\Users\mijaj\python\projects\student_performance_analyzer\student_data.csv")

top = df.sort_values("exam_score", ascending=False).head(20)

plt.figure(figsize=(10,6))
plt.plot(top["exam_score"].values, marker="o")
plt.grid(True)
plt.tight_layout()
plt.savefig(r"C:\Users\mijaj\python\projects\student_performance_analyzer\charts\top_students.png")
plt.show()