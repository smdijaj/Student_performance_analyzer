import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv(r"C:\Users\mijaj\python\projects\student_performance_analyzer\student_data.csv")

df["score_group"] = pd.cut(
    df["exam_score"],
    bins=[0, 50, 70, 85, 100],
    labels=["Poor", "Average", "Good", "Excellent"]
)

result = df.groupby("score_group")[[
    "study_hours",
    "attendance",
    "sleep_hours",
    "internet_usage"
]].mean()

plt.figure(figsize=(10,6))

for col in result.columns:
    plt.plot(result.index, result[col], marker="o", label=col)

plt.legend()
plt.grid(True)
plt.tight_layout()
plt.savefig(r"C:\Users\mijaj\python\projects\student_performance_analyzer\charts\behavior_comparison.png")
plt.show()