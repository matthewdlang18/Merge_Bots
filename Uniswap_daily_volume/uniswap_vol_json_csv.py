import pandas as pd
import json

with open("uniswapvolume.txt") as f:
    data = json.load(f)

df = pd.DataFrame(data["totalDataChart"], columns=["timestamp", "volume"])
df.to_csv("uniswapvolume.csv", index=False)
