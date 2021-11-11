import pandas as pd

a = pd.read_csv("reviews.csv")
a['Value']='R' #real reviews
a = a.dropna(axis=1)

b = pd.read_csv("fakereviews.csv")
b['Value']='F' #fake reviews
b = b.dropna(axis=1)

merged = a.merge(b, on='title')
merged.to_csv("reviews.csv", index=False)