import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv(r"C:\Users\mijaj\python\projects\student_performance_analyzer\student_data.csv")
numeric=df.select_dtypes(include=['int64','float64'])
corr=numeric.corr()
print(corr['exam_score'].sort_values(ascending=False))
plt.figure(figsize=(10,8))
plt.imshow(corr,interpolation='none')
plt.xticks(range(len(corr)), corr.columns, rotation=90  )
plt.yticks(range(len(corr)), corr.columns)
plt.colorbar()  
plt.tight_layout()
plt.savefig(r"C:\Users\mijaj\python\projects\student_performance_analyzer\charts\correlation_heatmap.png")
plt.show()