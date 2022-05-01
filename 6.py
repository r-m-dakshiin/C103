import pandas as pd
import plotly.express as px

df = pd.read_csv("data.csv")
fig = px.line(df, x='Population',y='Per capita')
fig.show()