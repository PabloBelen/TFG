import sys
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D
from Funciones import *


def PlanosZW(x,y,ptos,f):
    a = np.linspace(x[0], x[1], ptos[0])
    b = np.linspace(y[0], y[1], ptos[1])
    
    fig = plt.figure(figsize=(10,10))
    fig.subplots_adjust(hspace=0.5, wspace=0.5)
    ax = fig.add_subplot(1, 2, 1)
    for num in a:
        vals = np.ones(ptos[1])*num
        line = Line2D(vals, b, c = 'r')
        ax.add_line(line)
        line = Line2D(b, vals, c = 'm')
        ax.add_line(line)
    
    plt.plot(x[0],y[0],'b*', x[1],y[0],'k*', x[0],y[1],'y*', x[1],y[1],'g*')        
    plt.xlim(x[0]-1,x[1]+1)
    plt.xlabel('Re(z)')
    plt.ylim(y[0]-1,y[1]+1)
    plt.ylabel('Im(z)')
    plt.axis('scaled')
    plt.grid()
    
    ax = fig.add_subplot(1, 2, 2)
    ptos = []
    for num in a:
        vals1 = []
        vals2 = []
        for num2 in b:
            vals1.append(f(num + num2*1j))
            vals2.append(f(num2 + num*1j))
        ptos.append(vals1)
        ptos.append(vals2)
        vals1 = np.array(vals1)
        vals2 = np.array(vals2)
        line = Line2D(vals1.real, vals1.imag, c = 'r')
        ax.add_line(line)
        line = Line2D(vals2.real, vals2.imag, c = 'm')
        ax.add_line(line)
    
    ptos = np.array(ptos) 
    pto1 = f(x[0]+y[0]*1j)
    pto2 = f(x[1]+y[0]*1j)
    pto3 = f(x[0]+y[1]*1j)
    pto4 = f(x[1]+y[1]*1j)
    
    plt.plot(pto1.real,pto1.imag,'b*',pto2.real,pto2.imag,'k*',pto3.real,pto3.imag,'y*',pto4.real,pto4.imag,'g*') 
    plt.xlim(np.min(ptos.real)-1, np.max(ptos.real)+1)
    plt.xlabel('Re(w)')
    plt.ylim(np.min(ptos.imag)-1, np.max(ptos.imag)+1)
    plt.ylabel('Im(w)')
    plt.axis('scaled')
    plt.grid()
    plt.savefig('hola.png', dpi = 300, bbox_inches='tight',pad_inches = 0)
    plt.show()
    

PlanosZW([-3,3],[-3,3],[12,1000],f2)
PlanosZW([-np.pi,np.pi],[-np.pi,np.pi],[12,1000],cexp)


#Transformaciones fraccionales lineales
def TransfMobius(a,b,c,d):
    prod = a*d-b*c
    if prod == 0 + 0*1j:
        sys.exit('No se puede llevar a cabo la transformación de Möbius para los valores a = {}, b={}, c={}, d={}.'.format(a,b,c,d))
    def func(z):
        return (a*z + b)/(c*z + d)
    PlanosZW([-3,3], [-3,3], [12,1000], func)

TransfMobius(1,3,0,1)  #f(z)=z+3 traslación
TransfMobius(2,0,0,1)  #f(z)=2z homotecia
TransfMobius(1j,0,0,1)  #f(z)=iz rotación
TransfMobius(0,1,1,0)  #f(z)=1/z inversión y reflexión respecto eje real
TransfMobius(5,-1j,5*1j,1)  #f(z)=(5z-i)/(5iz+1) no funciona porque ad-bc=0 