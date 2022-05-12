import pandas as pd

 
def archivo():
  datos = pd.read_csv("vehicles_1500.csv")
  region = df.groupby("region").agg({"price" : 'mean', "year" : 'max'})
  model = df.groupby("model").agg({"price" : 'mean', "year" : 'max'})
  print(region)
  print(model) 

def main():
  archivo()