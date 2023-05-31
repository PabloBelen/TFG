import numpy as np
import matplotlib.pyplot as plt
from Funciones import *


def campovectores(x,y,ptos,f):
    a = np.linspace(x[0], x[1], ptos[0])
    b = np.linspace(y[0], y[1], ptos[1])
    A, B = np.meshgrid(a,b)
    func = funtomat2(A,B,f)
    u = func.real
    v = func.imag
    plt.figure(figsize = (10,10))
    plt.quiver(A, B, u, v, color = 'b')
    plt.xlim(x[0], x[1])
    plt.ylim(y[0], y[1])
    plt.grid()
    plt.show()
    

campovectores([-2, 2], [-2, 2], [25,25], f1)
campovectores([-2, 2], [-2, 2], [25,25], f2)
