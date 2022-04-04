##  importo libbrerie e funzioni che mi servono ##
import numpy as np                     #serve per generare le liste per gli intervalli
import matplotlib.pyplot as plt        #serve per plottare
from sympy import*
import sympy.printing as platex
import pandas as pd
import pdfkit

# definisco alcune funzioni #
def p_latex(a):
    return '$' + platex.latex(a) + '$'  #restituisce in scrittura latex a i caratteri '$' servono per l'interpretazione in latex 

##  definisco funzioni e variabili simboliche  ##
x = symbols('x')
f = 0.05*x + 0.2/((x - 5)**2 + 2)

## converto le funzioni simboliche in funzioni matematiche  ##
## in questo modo le posso calcolare in un'intervalo        ##
lam_f = lambdify(x, f, modules=['numpy'])   #converte la  funzione simbolica in funzione matematica

##  calcolo le funzioni in un'intervallo ##
x_plot = np.linspace(0, 10, 10)
f_plot = lam_f(x_plot)

#  scrive in un file html ed esporta in un pdf #
df = {'x_plot': x_plot, 'f_plot': f_plot}
df = pd.DataFrame(data=df)
f = open('exp.html','w')
a = df.to_html()
f.write(a)
f.close()

pdfkit.from_file('exp.html', 'example.pdf')     #NON VA

plt.show()                                     #mostra tutti i plot fatti