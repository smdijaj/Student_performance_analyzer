import pandas as pd

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

print(result.round(2))