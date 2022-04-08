import sympy as sy
import numpy as np

# questa libbreria serve per aggiungere funzioni alle classe sympy gia esistente #

# restituisce una funzione simbolica in formato numpy #
def matt(function_simbolic, parameter):
        return sy.lambdify (parameter, function_simbolic, modules=['numpy'])
        #return sympy.lambdify (parameter, function_simbolic, modules=['numpy']) #funzione con in formato matematico e non piu simbolico

# CALCOLO NUMERICO DI UNA FUNZIONE #
# claclolo numerico della funzione utilizzando il foramto numpy #
def calc(function_simbolic, parameter, *vaule):
        function_mat = matt(function_simbolic, parameter)
        # calcolo puntuale/intervallo passando una sola variabile #
        if len(vaule) == 1:
                return function_mat(vaule[0])
        # calcolo intervallo definendo l'intervallo nella funzione #
        else:
                a = np.linspace(vaule[0], vaule[1], vaule[2])
                return function_mat(a)