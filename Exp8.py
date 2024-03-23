import pandas as pd
import numpy as np
df = pd.read_excel("D:/Query Processing/SaleData.xlsx")
table = pd.pivot_table(df,index=["Region","Manager","SalesMan"], values="Sale_amt")
print(table.query('Manager == ["Douglas"]'))