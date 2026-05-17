import pandas as pd
import matplotlib.pyplot as plt 
df = pd.read_csv(r"C:\Users\mijaj\python\projects\student_performance_analyzer\student_data.csv")  
placement_counts = df["placement_status"].value_counts()
plt.figure(figsize=(6, 6))
plt.bar(placement_counts.index, placement_counts.values, color=['blue', 'orange'])
plt.title("Placement Status Distribution")
plt.xlabel("Placement Status")
plt.ylabel("Count")
plt.tight_layout()
plt.savefig(r"C:\Users\mijaj\python\projects\student_performance_analyzer\charts\placement_status_distribution.png")
plt.show()