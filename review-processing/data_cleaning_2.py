import pandas as pd

f1 = pd.read_csv("Group1.csv")
f1 = f1.dropna(axis=1)

f2 = pd.read_csv("Group2.csv")
f2 = f2.dropna(axis=1)

f3 = pd.read_csv("Group3.csv")
f3 = f3.dropna(axis=1)

f4 = pd.read_csv("Group4.csv")
f4 = f4.dropna(axis=1)

f5 = pd.read_csv("Group5.csv")
f5 = f5.dropna(axis=1)

f6 = pd.read_csv("Group6.csv")
f6 = f6.dropna(axis=1)

f7 = pd.read_csv("Group7.csv")
f7 = f7.dropna(axis=1)

f8 = pd.read_csv("Group8.csv")
f8 = f8.dropna(axis=1)

f9 = pd.read_csv("Group9.csv")
f9 = f9.dropna(axis=1)

merged = f1.append(f2)
merged = merged.append(f3)
merged = merged.append(f4)
merged = merged.append(f5)
merged = merged.append(f6)
merged = merged.append(f7)
merged = merged.append(f8)
merged = merged.append(f9)

merged.to_csv("all_reviews.csv", index=False)
sample = merged[merged['Label']=='F']
sample = sample.sample(n=10)
sample.to_csv("sampled_reviews.csv", index=False)