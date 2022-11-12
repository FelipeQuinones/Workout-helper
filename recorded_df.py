import pandas as pd
import numpy as np
import time

def pathTime():
    localtime = time.localtime()
    df_name = "{hour};{minute};{second}-{day}D-{month}M-{year}Y".format(hour=localtime[3], 
    minute=localtime[4], second=localtime[5], day=localtime[2], month=localtime[1], year=localtime[0])
    return str("Records/"+str(df_name)+".csv")

def createDf(weight1_name="Pesa 1", weight2_name="Pesa 2"):
    columns=[weight1_name, weight2_name]
    df = pd.DataFrame(columns=columns)
    return df

"""df1 = createDf()

for i in range(6):
    row = {"Peso 1":i, "Peso 2":i}
    df1 = df1.append(row, ignore_index=True)

df1.to_csv(pathTime())"""