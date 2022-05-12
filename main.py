import archivo

def archivo():
  df = pd.read_csv("vehicles(10k).csv")
  file = df.groupby("region").agg({"price" : 'mean'})
  print(file)