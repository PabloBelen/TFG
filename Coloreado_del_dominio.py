import sys
import numpy as np
import matplotlib.pyplot as plt 
from Funciones import *


def coloreado(x, y, ptos, func, **kwargs):
    opc = [k for k in kwargs]
    tipo = kwargs.get('tipo')
    escala = kwargs.get('escala')
    output = kwargs.get('output')
    if not 'tipo' in opc: tipo = 1
    if not 'escala' in opc: escala = 4
    if not 'output' in opc: output = False
    if tipo not in [1,2,3,4,5]:
        sys.exit('No se ha introducido un tipo de gráfica válido.')
    if tipo == 2 and escala not in [1,2,3,4]:
        sys.exit('No se ha introducido una escala para el tipo 2 de la gráfica válida.')
    
    if len(x) != 2 or len(y) != 2 or len(ptos) != 2:
        sys.exit('No se han introducido números de puntos adecuados.')
    a = np.linspace(x[0], x[1], ptos[0])
    b = np.linspace(y[0], y[1], ptos[1])
    A, B = np.meshgrid(a, b)
    f = funtomat2(A,B,func)
    dim = np.shape(f)

    arg = np.angle(f)
    arg[arg<0] += 2*np.pi
    hue = arg/(2*np.pi)
        
    mod = abs(f)
    vmin = np.min(mod)
    vmax = np.max(mod)
    print(vmin, vmax)

    if tipo == 1:  #retrato de fase
        lum = np.ones(dim)*0.5
    
    elif tipo == 2:  #retrato de fase con módulo identificado con luminosidad
        lum = np.copy(mod)
        
        if vmax == vmin:  #función constante
            lum = np.ones(dim)*0.5

        elif escala == 1:
            if vmax <= 5:
                lum = mod / vmax
            else:
                lum[np.abs(f) <= 1] *= 0.3  #valores módulo <=1 se les asigna luminosidad 0-0.3
                lum[(np.abs(f) > 1) & (np.abs(f) <= 0.5*vmax)] = 0.4 * (lum[(np.abs(f) > 1) & (np.abs(f) <= 0.5*vmax)] - 1) / (0.5*vmax - 1) + 0.3  #valores módulo en (1, vmax/2) se les asigna luminosidad 0.3-0.7
                lum[0.5*vmax < np.abs(f)] = 0.3 * (lum[0.5*vmax < np.abs(f)] - 0.5*vmax) / (0.5 * vmax) + 0.7  #valores módulo > vmax/2 se les asigna luminosidad 0.7-1

        elif escala == 2:
            lum[np.abs(f) <= 1] *= 0.3  #valores módulo <=1 se les asigna luminosidad 0-0.3
            lum[(1 < np.abs(f)) & (np.abs(f) <= vmax/100)] = 0.4 * (lum[(1 < np.abs(f)) & (np.abs(f) <= vmax/100)] - 1) / (vmax/100 - 1) + 0.3  #valores módulo (1, vmax/100], se les asigna luminosidad 0.3-0.7
            lum[vmax/100 < np.abs(f)] = 0.3 * (lum[vmax/100 < np.abs(f)] - vmax/100) / (vmax - vmax/100) + 0.7  #valores módulo > vmax/100 se les asigna luminosidad 0.7-1

        elif escala == 3: 
            a = float(input('Introduce el valor del módulo a representar con luminosidad 0.3: '))  #a > 0
            b = float(input('Introduce el valor del módulo a representar con luminosidad 0.7: '))  #b > a
            lum[np.abs(f) <= a] *= 0.3 / a  #valores módulo <=a se les asigna luminosidad 0-0.3
            lum[(np.abs(f) > a) & (np.abs(f) <= b)]  = 0.4 * (lum[(np.abs(f) > a) & (np.abs(f) <= b)] - a) / (b - a) + 0.3  #valores módulo (a, b] se les asigna luminosidad 0.3-0.7
            lum[b < np.abs(f)] = 0.3 * (lum[b < np.abs(f)] - b) / (vmax - b) + 0.7 #valores módulo > b se les asigna luminosidad 0.7-1
            
        elif escala == 4:
            a = float(input('Introduce el valor del módulo máximo a representar con luminosidad 0: '))
            b = float(input('Introduce el valor del módulo mínimo a representar con luminosidad 1: '))
            lum[np.abs(f) <= a] = 0  #valores módulo <=a se les asigna luminosidad 0
            lum[(np.abs(f) > a) & (np.abs(f) <= b)]  = (lum[(np.abs(f) > a) & (np.abs(f) <= b)] - a) / (b - a)  #valores módulo [a, b] se les asigna luminosidad 0-1
            lum[b < np.abs(f)] = 1  #valores módulo > b se les asigna luminosidad 1

    elif tipo == 3: #retrato de fase con líneas de contorno de fase
        lum = 0.1*(arg * 8 / np.pi - funtomat1(arg * 8 / np.pi, floor)) + 0.4 #rango luminosidad [0.4, 0.5]
        
    elif tipo == 4: #retrato de fase con líneas de contorno del módulo
        lum = 0.1*(funtomat1(mod, log) - funtomat1(mod, floorlog)) + 0.4 #rango luminosiad [0.4,0.5]
        
    elif tipo == 5: #retrato de fase con líneas de contorno de la fase y el módulo
        lum = 0.1*(arg * 8 / np.pi - funtomat1(arg * 8 / np.pi, floor)) + 0.1*(funtomat1(mod, log) - funtomat1(mod, floorlog)) + 0.3 #rango luminosidad [0.3,0.5]
                    
    sat = np.ones(dim)
    C = hls_rgb(hue, lum, sat)
    plt.figure()
    plt.imshow(C[::-1])
    plt.axis ('off')
    plt.savefig("coloreado", bbox_inches='tight',pad_inches = 0, dpi=1000)
    plt.show()
    
    if output == True:
        return C
    


#Retrato de fase
coloreado([-2,2], [-2,2], [2000,2000], f, tipo = 1) #para cualquier función compleja

#Retrato de fase con módulo identificado con luminosidad
coloreado([-2,2], [-2,2], [2000,2000], f, tipo = 2, escala = 1) #f, f1, f2, g6, f7, cexp, clog, csqrt, cthrt, csin, ccos, carcsin, carccos
coloreado([-2,2], [-2,2], [2000,2000], f3, tipo = 2, escala = 2) #f3, f4, f5, f6, f8, ctan, gamma
coloreado([-2*np.pi, 2*np.pi], [-2*np.pi, 2*np.pi], [2000,2000], polTaylor, tipo = 2, escala = 3) #a=0.5, b=30
coloreado([-1,1], [-1,1], [2000,2000], cexp2, tipo = 2, escala = 3) #a=1, b=1000
coloreado([-2*np.pi,2*np.pi], [-2*np.pi,2*np.pi], [2000,2000], gamma2, tipo = 2, escala = 3) #a=0.0001, b=10
coloreado([-17, 17], [-17, 17], [2000, 2000], zetariemann, tipo = 2, escala = 3) #a=1 y b=1000

#Retrato de fase con líneas de contorno de fase
coloreado([-2,2], [-2,2], [2000,2000], f, tipo = 3) #para cualquier función compleja

#Retrato de fase con líneas de contorno del módulo
coloreado([-2,2], [-2,2], [2000,2000], f, tipo = 4) #para cualquier función compleja

#Retrato de fase con líneas de contorno de la fase y el módulo
coloreado([-2,2], [-2,2], [2000,2000], f, tipo = 5) #para cualquier función compleja

#Otras gráficas
coloreado([-0.03, 0.03], [-0.03, 0.03], [2000, 2000], cexp2fase, tipo = 1) #zoom retrato fase singularidad esencial e^(1/z)
coloreado([-3, 4], [-2, 60], [700, 6200], zetariemann, tipo = 2, escala = 2)
coloreado([-11, 0.5], [-3, 3], [1250, 600], zetariemann, tipo = 2, escala = 3) #a=0.005 y b=0.1