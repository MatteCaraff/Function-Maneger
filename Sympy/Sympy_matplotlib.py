##  importo libbrerie e funzioni che mi servono ##
import numpy as np                     #serve per generare le liste per gli intervalli
import matplotlib.pyplot as plt        #serve per plottare
from sympy import symbols, Symbol, exp, integrate, lambdify, sin, sqrt, diff
import sympy.printing as platex
import pandas as pd

def p_latex(a):
    return '$' + platex.latex(a) + '$'  #restituisce in scrittura latex a i caratteri '$' servono per l'interpretazione in latex 

##  definisco funzioni e variabili simboliche  ##
x = symbols('x')
f = 0.05*x + 0.2/((x - 5)**2 + 2)
g = diff(f)
#g = (x**2)/3

## converto le funzioni simboliche in funzioni matematiche  ##
## in questo modo le posso calcolare in un'intervalo        ##
lam_f = lambdify(x, f, modules=['numpy'])   #converte la  funzione simbolica in funzione matematica
lam_g = lambdify(x, g, modules=['numpy'])

##  calcolo le funzioni in un'intervallo ##
x_plot = np.linspace(0, 10, 100)
f_plot = lam_f(x_plot)
g_plot = lam_g(x_plot)

plt.figure("grafici")                        #definisce una finestra di plot

##  polt di un grafico  ##
plt.plot(x_plot, f_plot, color="red")                     #plot grafico con i 2 assi si puo definire anche il colore della curva
plt.plot(x_plot, g_plot, color="magenta")
plt.legend([p_latex(f), p_latex(g)], loc ="upper left")   #plot della legenda inserire in ordine i elementi del grafico si puo definire la sua posizione
plt.xlabel("asse x")                                      #plot del nome asse x
plt.ylabel("asse y")
plt.title("titolo grafico")                               #plot titolo grafico

#  creazione datafreme  che viene usato solo per il plot  #
df = {'x_plot': x_plot, 'f_plot': f_plot}
df = pd.DataFrame(data=df)

""" # plot della tabella a schermo #
fig, ax = plt.subplots()                                                                         #crea un subplot
fig.suptitle('tabella', fontsize=16)                                                             #aggiunge un sottotitolo
ax.axis('off')                                                                                   #toglie gli assi alla figura
tabella = ax.table(cellText=df.values, cellLoc="right", colLabels=df.columns, loc='center')      #definisco la tabella

# autoformato la tabella in funzione del fontsize #
def format_table(table, fontsize):
    table.set_fontsize(fontsize)                        
    x=(1/34)*fontsize
    y=(2/34)*fontsize
    table.scale(x, y)
    
format_table(tabella, 34) """


plt.show()                               #mostra tutti i plot fatti