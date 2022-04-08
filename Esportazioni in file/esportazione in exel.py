import pandas as pd
from numpy import *
# pip install openpyxl #

# create dataframe
x = linspace(0, 10, 10)
y = linspace(-10, 0, 10)
df = {'x': x, 'f': y}
df = pd.DataFrame(data=df)

# create excel writer object
writer = pd.ExcelWriter('output.xlsx')
# write dataframe to excel
df.to_excel(writer)
# save the excel
writer.save()