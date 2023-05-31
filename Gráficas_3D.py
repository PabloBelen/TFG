import sys
import numpy as np
import matplotlib.pyplot as plt
from Funciones import *
from Coloreado_del_dominio import coloreado


def grafica3D(x, y, ptos, func, **kwargs):
    
    opc=[k for k in kwargs] 
    tipo = kwargs.get('tipo')
    zlim = kwargs.get('zlim')
    view = kwargs.get('view')
    if not 'tipo' in opc: tipo = 'mod'
    if not 'view' in opc: view = [0,0]
    if tipo not in ['real','imag','mod']:
        sys.exit('No se ha introducido un tipo de gráfica válido.')
        
    a = np.linspace(x[0],x[1],ptos[0]);
    b = np.linspace(y[0],y[1],ptos[1]);
    A, B = np.meshgrid(a,b); 
    z = A+1j*B; 
    f = funtomat2(A, B, func)
    
    fig = plt.figure(figsize = (20,20), dpi = 300)
    ax = fig.add_subplot(111, projection = '3d')
    ax.view_init(view[0],view[1])
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    
    if tipo == 'real':
        real = f.real
        if not 'zlim' in opc: zlim = np.max(np.abs(real))
        real[(real < -zlim) | (real > zlim)] = np.nan
        ax.plot_surface(z.real, z.imag, real)
        ax.set_zlabel('Re(f(z))')
            
    elif tipo == 'imag':
        imag = f.imag
        if not 'zlim' in opc: zlim = np.max(np.abs(imag))
        imag[(imag < -zlim) | (imag > zlim)] = np.nan
        ax.plot_surface(z.real, z.imag, imag)
        ax.set_zlabel('Im(f(z))')
            
    elif tipo == 'mod':
        mod = abs(f)
        if not 'zlim' in opc: zlim = np.max(mod)
        mod[mod > zlim] = np.nan 
        ax.plot_surface(z.real, z.imag, mod)
        ax.set_zlabel('|f(z)|')            
        ax.set_zlim(0,zlim)
        
    plt.show()
    
def grafica3Dcoloreada(x, y, ptos, func, **kwargs):
    opc = [k for k in kwargs]
    tipo = kwargs.get('tipo')
    escala = kwargs.get('escala')
    zlim = kwargs.get('zlim')
    view = kwargs.get('view')
    if not 'tipo' in opc: tipo = 1
    if not 'escala' in opc: escala = 4
    if not 'view' in opc: view = [0,0]
    if len(x) != 2 or len(y) != 2 or len(ptos) != 2:
        sys.exit('No se han introducido valores adecuados.')
        
    a = np.linspace(x[0], x[1], ptos[0])
    b = np.linspace(y[0], y[1], ptos[0])
    A, B = np.meshgrid(a, b)
    f = funtomat2(A,B,func)
    
    img = coloreado(x, y, ptos, func, tipo = tipo, escala = escala, output = True)
    fig = plt.figure(figsize = (30,45), dpi = 300)
    ax = fig.add_subplot(1, 1, 1, projection = "3d")
    ax.view_init(view[0], view[1])
    mod = abs(f)
    if not 'zlim' in opc: zlim = np.max(mod)
    mod[mod > zlim] = np.nan 
    ax.plot_surface(A, B, mod, facecolors = img, rstride = 2, cstride = 2 )
    ax.set_zlim([0, zlim])
    plt.show()
        


#Superficies analíticas de gamma(z)
grafica3D([-5.5,5.5], [-4,4], [1000, 1000], gamma, tipo = 'mod', zlim = 8, view = [15, 240])
grafica3Dcoloreada([-5.5,5.5], [-4,4], [1000,1000], gamma, tipo = 1, zlim = 8, view = [15, 240])


#Gráficas 3D función z^2
grafica3D([-2,2], [-2,2], [1000, 1000], f2, tipo = 'real', view = [35, 290])
grafica3D([-2,2], [-2,2], [1000, 1000], f2, tipo = 'imag', view = [35, 290])
grafica3D([-2,2], [-2,2], [1000, 1000], f2, tipo = 'mod', zlim = 8, view = [35, 290])

a = np.linspace(-2,2,1000);
b = np.linspace(-2,2,1000);
A, B = np.meshgrid(a,b); 
z = A+1j*B; 
f = funtomat2(A, B, f2)
Arg = np.angle(f)
Arg[np.abs(z.real) < 0.01] = np.nan 
fig = plt.figure(figsize = (20,20), dpi = 300)
ax = fig.add_subplot(111, projection = '3d')
ax.view_init(35,290)
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.plot_surface(z.real, z.imag, Arg)
ax.set_zlabel('Arg(z)')


#Superficie analítica coloreada de exp(1/z)
grafica3Dcoloreada([-2,2], [-2,2], [1000,1000], cexp2, tipo = 1, zlim = 6, view = [15, 240])




