import sympy
import numpy

# la classe che seggue è scritta per gestire una funzione matematica dal formato simbolico #
# della libbreria sympy con il formato matematico integrato in python. I risultati di questa #
# libbreria saranno in formato lista #

class Function(sympy, numpy):
    
    def __init__(self, funct_simbol):
        self._funct_simbol = funct_simbol
    
    def get_funct_simbol(self):
        return self._funct_simbol

    def _mat_(self, parameter):
        return sympy.lambdify (parameter, self._funct_simbol, modules=['numpy']) #funzione con in formato matematico e non piu simbolico

     # metodi per la gestione della funzione #
    
    def calc(self, parameter, vaule):                           #calcolo la funzione in un punto
        function_mat = self._mat_(parameter)
        return function_mat(vaule)

    def calc(self, parameter, inizio, fine, intervallo):        #calcolo della funzione in un' intervallo numerico
        function_mat = self._mat_(parameter)
        a = numpy.linspace(inizio, fine, intervallo)
        return function_mat(a)                           #lista che contiene la funzione calcolata nell' intervallo