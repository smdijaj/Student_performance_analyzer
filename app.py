from flask import Flask, request
import pandas as pd
import matplotlib.pyplot as plt

app = Flask(__name__)

@app.route("/")
def home():
    group = request.args.get("group")
    min_score = request.args.get("min_score")

    df = pd.read_csv(r"C:\Users\mijaj\python\projects\student_performance_analyzer\student_data.csv")

    df["score_group"] = pd.cut(
        df["exam_score"],
        bins=[0, 50, 70, 85, 100],
        labels=["Poor", "Average", "Good", "Excellent"]
    )

    filtered = df.copy()

    if group:
        filtered = filtered[
            filtered["score_group"].astype(str).str.lower() == group.lower().strip()
        ]

    if min_score:
        filtered = filtered[
            filtered["exam_score"] >= float(min_score)
        ]

    if not filtered.empty:
        result = filtered.groupby("score_group")[
            ["study_hours", "attendance", "sleep_hours", "internet_usage"]
        ].mean()

        plt.figure(figsize=(10,6))

        for col in result.columns:
            plt.plot(result.index.astype(str), result[col], marker="o", label=col)

        plt.legend()
        plt.grid(True)
        plt.tight_layout()
        plt.savefig(r"C:\Users\mijaj\python\projects\student_performance_analyzer\static\live_chart.png")
        plt.close()

    avg_score = filtered["exam_score"].mean() if not filtered.empty else 0
    highest = filtered["exam_score"].max() if not filtered.empty else 0
    lowest = filtered["exam_score"].min() if not filtered.empty else 0

    html = f"""
    <h1>Student Performance Dashboard</h1>

    <form>
        <input name="group" placeholder="Poor / Average / Good / Excellent">
        <input name="min_score" placeholder="Minimum score">
        <button type="submit">Filter</button>
    </form>

    <div style="display:flex; gap:30px; margin:20px 0;">
        <div><b>Total:</b> {len(filtered)}</div>
        <div><b>Average:</b> {avg_score:.2f}</div>
        <div><b>Highest:</b> {highest}</div>
        <div><b>Lowest:</b> {lowest}</div>
    </div>

    <div style="display:flex; gap:20px; align-items:flex-start;">
        <img src="/static/live_chart.png" width="650">
        {filtered.head(20).to_html(index=False)}
    </div>
    """

    return html

if __name__ == "__main__":
    app.run(debug=True)