import pandas as pd
import plotly.express as ps
df=pd.read_csv("C:/Users/mhrat/Downloads/python/c104/csv files/data.csv")
graph =ps.bar(df,x='Country',y='Population')
graph.show()

