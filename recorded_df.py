import pandas as pd
import numpy as np
import pathlib as Path
import time


x = int(input())

localtime = time.localtime()
df_name = "{hour};{minute};{second}-{day}D-{month}M-{year}Y".format(hour=localtime[3], 
minute=localtime[4], second=localtime[5], day=localtime[2], month=localtime[1], year=localtime[0])
path_ = str("Records/"+str(df_name)+".csv")

weight1_name, weight2_name = "Peso 1", "Peso 2"
columns=[weight1_name, weight2_name]
df = pd.DataFrame(columns=columns)

for i in range(x):
    row = {weight1_name:i, weight2_name:i}
    df = df.append(row, ignore_index=True)

df.to_csv(path_)
