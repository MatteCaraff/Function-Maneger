##  importo libbrerie e funzioni che mi servono ## 
from sympy import *                                                 #importo i metodi e le funzione da sympy per comodità di scrittura del codice
#from sympy import Symbol, exp, evalf, integrate, lambdify, sin, sqrt, diff       

##  definizione variabile simbolica e funzione  ##
x=Symbol('x')      #variabile simbolica
f=x/2              #funzione

##  calcolo derivata e integrale indefinito ##
fd=diff(f, x, 1)    #derivata di ordine 1
F=integrate(f,x)    #integrale indefinito

##  calcolo puntuale  ##
y=f.subs(x, 1)           #sostituisce un numero oppure un'altra variabile alla variabile simbolica x
y=float(f.subs(x,1))     #converto in un float
y.evalf(2)               #dà un float con il numero di deciamali    ATTENZIONE METODO DI SYMPY

##  converssione funzione sympy in una funzione matematica  ##
y=lambdify(x, f)         #converto la funzione f definita sopra
print(y)