import pandas as pd
import plotly.express as px

df = pd.read_csv('line_chart.csv')
fig = px.line(df, x="Country",y="Year")
fig.show()