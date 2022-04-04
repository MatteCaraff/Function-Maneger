##  importo libbrerie e funzioni che mi servono ##
from Function import *
import pandas as pd

import sympy.printing as platex        #serve per esportare il latex le funzioni dell sympy
import pdfkit                          #esportazione in file html e in file pdf


# definisco alcune funzioni #
def p_latex(a):
    return '$' + platex.latex(a) + '$'      #restituisce in scrittura latex a i caratteri '$' servono per l'interpretazione in latex 

## definisco funzioni e variabili simboliche ##
x = symbols('x')
f = 0.05*x + 0.2/((x - 5)**2 + 2)

## calcolo le funzioni in un'intervallo e le inserisco in ##
## dataframe con il modulo pandas ##
intervallo = linspace(0, 10, 10)
f_intervallo = calc(f, x, 0, 10, 10)
#f_intervallo = calc_interval(f, x, intervallo)              #guarda nota file Function
df = {'x': intervallo, 'f': f_intervallo}
df = pd.DataFrame(data=df)


# scrive in un file html ed esporta in un pdf #
f = open('exp.html','w')            #inizio file htlm
a = df.to_html()
f.write(a)
f.close()                           #fine file html

pdfkit.from_file('exp.html', 'example.pdf')     #NON VA dovrebbe esportare l'html in un pdf