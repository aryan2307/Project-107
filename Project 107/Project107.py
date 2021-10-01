import pandas as pd
import plotly.express as px
df = pd.read_csv(r"C:/Users/Admin/Downloads/Practice/csv files/class107.csv")
fig = px.scatter(df, x = 'student_id', y = 'level', color = 'cleared')
fig.show()