import pandas as pd

df = pd.read_csv("./tk.csv", encoding="UTF-8", index_col=0)
df.to_json("./nest.json")
