from sympy import *     # introdotti solo per non scriverlo nel main preferisco usare la sintassi con il punto #
from numpy import *     # per saperer da dove arriva il metodo #

import sympy
import numpy

# questa libbreria serve per aggiungere funzioni alle classe sympy gia esistente #

# restituisce una funzione simbolica in formato numpy #
def mat(function_simbolic, parameter):
        return sympy.lambdify (parameter, function_simbolic, modules=['numpy']) #funzione con in formato matematico e non piu simbolico

# CALCOLO NUMERICO DI UNA FUNZIONE #
# claclolo la funzione in un punto utilizzando il foramto numpy #
def calc(function_simbolic, parameter, vaule):
        function_mat = mat(function_simbolic, parameter)
        return function_mat(vaule)

# calcolo la funzione in un intervallo utilizzanto il modulo numpy # 
def calc(function_simbolic, parameter, start, end, interval):
        function_mat = mat(function_simbolic, parameter)
        a = numpy.linspace(start, end, interval)
        return function_mat(a)

def calc_interval(function_simbolic, parameter, interval):               #duale alla precedente ma si passa direttamente l'intervallo sotto forma di lista della numpy
        function_mat = mat(function_simbolic, parameter)                 #vorrei usare lo stesso nome della funzione come per una classe è possibile?
        return function_mat(interval)