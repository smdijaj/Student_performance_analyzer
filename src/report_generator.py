import pandas as pd

df = pd.read_csv( r"C:\Users\mijaj\python\projects\student_performance_analyzer\student_data.csv")

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
]].mean().round(2)

with open(r"C:\Users\mijaj\python\projects\student_performance_analyzer\reports\analysis_report.txt", "w") as f:
    f.write("Student Performance Analysis Report\n\n")
    f.write(str(result))
    f.write("\n\nKey Findings:\n")
    f.write("- Study hours strongly influence performance\n")
    f.write("- Attendance improves outcomes\n")
    f.write("- High internet usage correlates negatively\n")
    f.write("- Better students sleep slightly more\n")

print("Report created")