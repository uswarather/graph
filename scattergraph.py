import pandas as pd
import plotly_express as ps
df = pd.read_csv('C:/Users/mhrat/Downloads/python/c104/csv files/Copy+of+data+-+data.csv')
graph=ps.scatter(df,x="date",y="cases",color="country")
graph.show()
