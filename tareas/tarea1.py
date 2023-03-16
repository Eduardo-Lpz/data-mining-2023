import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

names = ["sepal_length_in_cm", "sepal_width_in_cm", "petal_length_in_cm", "petal_width_in_cm", "species"]

df = pd.read_csv("./datasets/iris.data", header=None, names=names)
df.species = df.species.astype("category")

print("vista rapida de los datos")
print(df.head())

print("largo y ancho promedio de petalo y sepalo")
print(df.describe().loc[["mean"]])

df.species.value_counts().plot(kind="bar")
plt.show()

df.plot.scatter(x="sepal_length_in_cm", y="sepal_width_in_cm", c="species", cmap="viridis")
plt.show()
