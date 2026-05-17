from flask import Flask, request
import pandas as pd

app = Flask(__name__)

@app.route("/")
def home():
    group = request.args.get("group")
    chart = request.args.get("chart", "behavior_comparison.png")

    df = pd.read_csv(r"C:\Users\mijaj\python\projects\student_performance_analyzer\student_data.csv")

    df["score_group"] = pd.cut(
        df["exam_score"],
        bins=[0, 50, 70, 85, 100],
        labels=["Poor", "Average", "Good", "Excellent"]
    )

    if group:
        filtered = df[df["score_group"].astype(str).str.lower() == group.lower()]
    else:
        filtered = df

    html = f"""
    <h1>Student Performance Dashboard</h1>

    <form>
        <input name="group" placeholder="Poor / Average / Good / Excellent">
        <button type="submit">Filter</button>
    </form>

    <p>
        <a href="/?chart=behavior_comparison.png">Behavior</a> |
        <a href="/?chart=top_students.png">Top Students</a>
    </p>

    <h3>Total Students: {len(filtered)}</h3>
    <h3>Average Score: {filtered['exam_score'].mean():.2f}</h3>

    <div style="display:flex; gap:20px;">
        <img src="/static/{chart}" width="650">
        {filtered.head(20).to_html(index=False)}
    </div>
    """

    return html

if __name__ == "__main__":
    app.run(debug=True)