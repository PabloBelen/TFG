import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
from Funciones import *

#Gráfica (x,y,v) de log(z) con ramas coloreadas
n = 3000
v = 4
a = np.linspace(-1, 1, n)
X, Y = np.meshgrid(a, a)
A, B = np.copy(X), np.copy(Y)
for i in range(v-1):
    A = np.concatenate((A,X))
    B = np.concatenate((B,Y))

Z = np.ones((n*v,n))*1j
for i in range(0,v):
    for j in range(len(X)):
        for k in range(len(X[j])):
            Z[j + i*n,k] = clog(X[j,k] + Y[j,k]*1j, p = i)
Z[(A**2 + B**2) > 1] = np.nan + np.nan*1j

fig = plt.figure(figsize = (20,20), dpi = 300)
ax = fig.add_subplot(111, projection = '3d')
ax.view_init(15,60)
colores = ['cyan', 'magenta', 'red', 'green']
for i in range(v):
    ax.scatter(A[i*n:(i+1)*n,], B[i*n:(i+1)*n,], Z.imag[i*n:(i+1)*n,], s = 0.02, c = colores[i%4], edgecolor = 'none')
for num in [-3,-2,-1,-0.5,0]:
    M = np.copy(Z)
    M[(Z.real < num - 0.005 + num*0.001) | (num + 0.005 + num*0.001 < Z.real)] = np.nan + np.nan*1j
    ax.scatter(A, B, M.imag, s = 0.5, c = 'k')
ax.set_xlim([-1, 1])
ax.set_ylim([-1, 1])
ax.set_zlim([0, 2*np.pi*(v-1)])
plt.savefig('3d.png')
plt.show()


#Gráfica (x,y,u) de sqrt(z) con color dado por v
n = 1500
a = np.linspace(-1, 1, n)
X, Y = np.meshgrid(a, a)
A = np.concatenate((X,X))
B = np.concatenate((Y,Y))

Z2 = np.ones((2*n,n))*1j
for i in range(0,2):
    for j in range(len(X)):
        for k in range(len(X[j])):
            Z2[j + i*n,k] = csqrt(X[j,k] + Y[j,k]*1j) * (-1)**i
           
print(np.min(Z2.imag), np.max(Z2.imag))
colores = mpl.cm.brg((Z2.imag-np.min(Z2.imag))/(np.max(Z2.imag)-np.min(Z2.imag)))
for num in [-1,-3/4,-1/2,-1/4,0,1/4,1/2,3/4,1]:
    colores[( num - 0.003 < Z2.imag) & (Z2.imag < num + 0.003)] = np.array([0,0,0,1])
lista = []
for fila in colores:
    for elem in fila:
        lista.append(elem)
        
fig = plt.figure(figsize = (20,20), dpi = 300)
ax = fig.add_subplot(111, projection='3d')
ax.view_init(20,225)
gr = ax.scatter(A, B, Z2.real, s= 0.5, c=lista, edgecolors = 'none')
ax.set_xlim([-1, 1])
ax.set_ylim([-1, 1])
gr.set_cmap('brg')
plt.colorbar(gr)  #0 corresponde a np.min(Z2.imag)=-1.0987 y 1 corresponde a np.max(Z2.imag)=1.0987
plt.savefig('3d.png')
plt.show()


#Gráfica (x,y,u) de cthrt(z) con color dado por v
n = 2000
a = np.linspace(-1, 1, n)
X, Y = np.meshgrid(a, a)
A = np.concatenate((X,X,X))
B = np.concatenate((Y,Y,Y))

Z3 = np.ones((3*n,n))*1j
for i in range(0,3):
    for j in range(len(X)):
        for k in range(len(X[j])):
            Z3[j + i*n,k] = cthrt(X[j,k] + Y[j,k]*1j, k = i) 
           
print(np.min(Z3.imag), np.max(Z3.imag))
colores = mpl.cm.brg((Z3.imag-np.min(Z3.imag))/(np.max(Z3.imag)-np.min(Z3.imag)))
for num in [-1,-3/4,-1/2,-1/4,0,1/4,1/2,3/4,1]:
    colores[( num - 0.003 < Z3.imag) & (Z3.imag < num + 0.003)] = np.array([0,0,0,1])
lista = []
for fila in colores:
    for elem in fila:
        lista.append(elem)
        
fig = plt.figure(figsize = (20,20), dpi = 300)
ax = fig.add_subplot(111, projection = '3d')
ax.view_init(20, 225)
gr = ax.scatter(A, B, Z3.real, s = 0.5, c = lista, edgecolors = 'none')
ax.set_xlim([-1, 1])
ax.set_ylim([-1, 1])
gr.set_cmap('brg')
plt.colorbar(gr)  #0 corresponde a np.min(Z2.imag)=-1.0842 y 1 corresponde a np.max(Z2.imag)=1.0842
plt.savefig('3d.png')
plt.show()


#Gráfica (x,y,u) de arcsen(z) con color dado por v
n = 1500
v = 4
a = np.linspace(-5, 5, n)
X, Y = np.meshgrid(a, a)
A, B = np.copy(X), np.copy(Y)
for i in range(v-1):
    A = np.concatenate((A,X))
    B = np.concatenate((B,Y))
    
Z4 = np.ones((v*n,n))*1j        
for i in range(0,v):
    for j in range(len(X)):
        for k in range(len(X[j])):
            w = X[j,k] + Y[j,k]*1j
            Z4[j+i*n,k] = -1j*clog(1j*w+csqrt(1-w**2)*(-1)**i, p = i//2)
                                 
print(np.min(Z4.imag), np.max(Z4.imag))
colores = mpl.cm.brg((Z4.imag-np.min(Z4.imag))/(np.max(Z4.imag)-np.min(Z4.imag)))
for num in [-2,-1,0,1,2]:
    colores[( num - 0.005 < Z4.imag) & (Z4.imag < num + 0.005)] = np.array([0,0,0,1])
lista = []
for fila in colores:
    for elem in fila:
        lista.append(elem)
        
fig = plt.figure(figsize = (20,20), dpi = 300)
ax = fig.add_subplot(111, projection='3d')
ax.view_init(15,135)
gr = ax.scatter(A, B, Z4.real, s= 0.5, c=lista, edgecolors = 'none')
ax.set_xlim([-5, 5])
ax.set_ylim([-5, 5])
gr.set_cmap('brg')
plt.colorbar(gr)  #0 corresponde a np.min(Z4.imag)=-2.649196177806471 y 1 corresponde a np.max(Z4.imag)=2.649196177806484 
plt.savefig('3d.png')
plt.show()


#Gráfica (x,y,u) de arccos(z) con color dado por v
n = 1500
v = 4
a = np.linspace(-5, 5, n)
X, Y = np.meshgrid(a, a)
A, B = np.copy(X), np.copy(Y)
for i in range(v-1):
    A = np.concatenate((A,X))
    B = np.concatenate((B,Y))
    
Z5 = np.ones((v*n,n))*1j        
for i in range(0,4):
    for j in range(len(X)):
        for k in range(len(X[j])):
            w = X[j,k] + Y[j,k]*1j
            Z5[j+i*n,k] = -1j*clog(w+csqrt(w**2-1)*(-1)**i, p = i//2)       
                      
print(np.min(Z5.imag), np.max(Z5.imag))
colores = mpl.cm.brg((Z5.imag-np.min(Z5.imag))/(np.max(Z5.imag)-np.min(Z5.imag)))
for num in [-2,-1,0,1,2]:
    colores[( num - 0.005 < Z5.imag) & (Z5.imag < num + 0.005)] = np.array([0,0,0,1])
lista = []
for fila in colores:
    for elem in fila:
        lista.append(elem)
        
fig = plt.figure(figsize = (20,20), dpi = 300)
ax = fig.add_subplot(111, projection='3d')
ax.view_init(15,315)
gr = ax.scatter(A, B, Z5.real, s= 0.5, c=lista, edgecolors = 'none')
ax.set_xlim([-5, 5])
ax.set_ylim([-5, 5])
gr.set_cmap('brg')
plt.colorbar(gr)  #0 corresponde a np.min(Z4.imag)=-2.65 y 1 corresponde a np.max(Z4.imag)=2.65
plt.savefig('3d.png')
plt.show()