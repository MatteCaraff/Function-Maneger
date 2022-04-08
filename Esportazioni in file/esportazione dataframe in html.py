##  importo libbrerie e funzioni che mi servono ##
from numpy import *
import pandas as pd
import pdfkit                          #esportazione in file html e in file pdf

config = pdfkit.configuration(wkhtmltopdf = r"D:\\Program Files\\wkhtmltopdf\\bin\\wkhtmltopdf.exe")   #dove è installata wkhtmltopdf

## creo un dataframe ##
x = linspace(0, 10, 10)
y = linspace(-10, 0, 10)
df = {'x': x, 'f': y}
df = pd.DataFrame(data=df)

# scrive in un file html ed esporta in un pdf #
f = open('exp.html','w')            #inizio file htlm
a = df.to_html()
f.write(a)
f.close()                           #fine file html