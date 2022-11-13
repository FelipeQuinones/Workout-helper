import pandas as pd
import numpy as np
import time

def dfPath():
    localtime = time.localtime()
    df_name = "{hour};{minute};{second}-{day}D-{month}M-{year}Y".format(hour=localtime[3], 
    minute=localtime[4], second=localtime[5], day=localtime[2], month=localtime[1], year=localtime[0])
    return str("Records/"+str(df_name)+".csv")

def createDf(weight1_name="Pesa 1", weight2_name="Pesa 2"):
    columns=[weight1_name, weight2_name]
    df = pd.DataFrame(columns=columns)
    return df

def addRow(df, peso1=0, peso2=0):
    row = pd.DataFrame([[peso1, peso2]],columns=["Pesa 1", "Pesa 2"])
    df = pd.concat([df, row], ignore_index=True)
    return df  

"""df1 = createDf()
for i in range(6):
    df1 = addRow(df1, 5, 5)

df1.to_csv(dfPath())"""