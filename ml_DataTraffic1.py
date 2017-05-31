import numpy as np
import pandas as pd


df1 = pd.read_csv("test.csv")

df1 = [i.split('\t  \t',1)[0] for i in df1]

print(df1)
