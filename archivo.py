import pandas as pd
import matplotlib.pyplot as plt

 
def archivo():
  pd.options.display.max_rows = 1500
  pd.options.display.startup(27)
  datos = pd.read_csv("vehicles(1500).csv")
  region = df.groupby("region").agg({"price" : 'mean', "year" : 'max'})
  model = df.groupby("model").agg({"price" : 'mean', "year" : 'max'})
  print(region)

 
def Dartabla():
print(datos)

def Promediodinero():
print(["price"].mean())

def Promediodineroxcolor():
  for i in ["colour"]:
    if color == "green":
     color = df.groupby("colour").agg({"price" : 'mean'})
    elif  color == "red":
     color = df.groupby("colour").agg({"price" : 'mean'})
