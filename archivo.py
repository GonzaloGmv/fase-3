import pandas as pd
import matplotlib.pyplot as plt

 
def archivo():
  pd.options.display.max_rows = 1500
  datos = pd.read_csv("vehicles(1500).csv")
  region = df.groupby("region").agg({"price" : 'min', "year" : 'max'})
  model = df.groupby("model").agg({"price" : 'min', "year" : 'max'})

 
def Dartabla:
print(datos)

def Promediodinero:
print(["price"].mean())