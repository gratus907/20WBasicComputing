import pandas as pd
df = pd.read_csv("gapminder.tsv", sep = "\t")

# (a)
print(df['country'])

# (b)
print(df[['country', 'continent', 'year']])

# (c)

print(df.iloc[0])
# (d)
print(df.iloc[[2, 4, 6]])

# (e)
print(df.iloc[[3, 4, 5]])

# (f)
print(df.iloc[[7, 8, 9, 10], [0, 3, 5]])

# (g)
print(df.iloc[[1, 3, 5], [0, 1, 4]])