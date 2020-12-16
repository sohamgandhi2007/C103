import pandas as pd
import plotly.express as px

df=pd.read_csv("c.csv")
fig=px.bar(df,x="Date",y="Cases",color="Country")
fig.show()