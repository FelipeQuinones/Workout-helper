import pandas as pd
import numpy as np
import time

def pathTime():
    localtime = time.localtime()
    df_name = "{hour};{minute};{second}-{day}D-{month}M-{year}Y".format(hour=localtime[3], 
    minute=localtime[4], second=localtime[5], day=localtime[2], month=localtime[1], year=localtime[0])
    return str("Records/"+str(df_name)+".csv")

def createDf(wght1="Pesa 1", wght2="Pesa 2"):
    weight1_name, weight2_name = wght1, wght2
    columns=[weight1_name, weight2_name]
    df = pd.DataFrame(columns=columns)
    return df

df1 = createDf()

for i in range(x):
    row = {"Peso 1":i, "Peso 2":i}
    df1 = df1.append(row, ignore_index=True)

df1.to_csv(pathTime())