import pandas as pd

data = pd.read_csv("./iris.csv")

pd.set_option("display.width", 100)
pd.set_option("display.max_columns", 100)
pd.set_option("display.max_rows", 250)



print(data)
print(data.head())
print(data.shape)
print(data.columns)
print(data.info())
print(data.describe())
print(data.describe(include = ["object", "bool"]))
print(data["species"].value_counts())
print(data["sepal_width"].value_counts(normalize = True))
data["species"] = pd.factorize(data["species"])[0]

