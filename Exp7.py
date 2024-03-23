import pandas as pd
import numpy as np
df = pd.read_excel("D:/Query Processing/SaleData.xlsx")
table = pd.pivot_table(df, index='Item', values='Sale_amt', aggfunc=[np.max, np.min])
print(table)
