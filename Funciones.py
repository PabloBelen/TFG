import sys
import math as mat
import cmath as com
import numpy as np
from mpmath import zeta
import scipy.special as sp
from colorsys import hls_to_rgb


#Funciones auxiliares
def log(x):
    return mat.log(x, 1.5)

def floorlog(x):
    return mat.floor(mat.log(x, 1.5))

def floor(x):
    return mat.floor(x)

def funtomat1(A,f):
    mat = np.ones(np.shape(A))
    for i in range(0,len(A)):
        for j in range(0,len(A[0])):
            mat[i,j]=f(A[i,j])
    return mat

def funtomat2(A,B,f):
    mat = np.ones(np.shape(A))*1j
    for i in range(0,len(A)):
        for j in range(0,len(A[0])):
            mat[i,j]=f(A[i,j]+B[i,j]*1j)
    return mat

def hls_rgb(H,L,S):
    dim1, dim2, dim3 = np.shape(H), np.shape(L), np.shape(S)
    if dim1 == dim2 and dim1 == dim3:
        C = []
        for i in range(len(H)):
            C.append([])
            for j in range(len(H[0])):
                col = hls_to_rgb(H[i, j], L[i, j], S[i, j])
                C[i].append([col[0], col[1], col[2]])
    else:
        sys.exit('No se puede usar la función hls_rgb en este caso.')
    return C



#Funciones complejas analíticas 
def f(z):
    return 1

def f1(z):
    return z

def f2(z):
    return z**2

def f3(z):
    return z**(-1)

def f4(z):
    return z**(-2)

def f5(z):
    return (z-(1-1j))*(z-(1+1j))/(z+1)**2

def f6(z):
    return 1/(z**6 - 1)

def f7(z): #f principio argumento
    return z*(z+1)*(z-1)**2

def f8(z): #h principio argumento
    return (z*(z+1)*(z-1)**2)/(((z-1j)**2)*(z+1j))

def cexp(z):
    return com.exp(z)

def polTaylor(z):
    val = 0
    for i in range(0,7):
        val += z**i/mat.factorial(i)
    return val

def cexp2(z):
    if z == 0:
        return com.inf
    elif abs(z) < 0.0015: #para z tales que 0<|z|<0.0015 damos el valor aproximado por la serie de Laurent de exp(1/z) en z
        val = 0
        for i in range(0,1000): 
            if mat.factorial(i)*(z**i) != 0:
                val += 1/(mat.factorial(i)*(z**i))
            else: 
                break
        return val
    else:
        return com.exp(1/z)
    
def cexp2fase(z):
    return ccos((1/z).imag) + 1j*csin((1/z).imag)
    
def clog(z, **kwargs):
    opc = [k for k in kwargs]
    p = kwargs.get('p')
    if not 'p' in opc: p = 0
    if type(p) != int:
        sys.exit('No se ha introducido un valor de p adecuado.')
    return com.log(z) + 2*p*mat.pi*1j

def csqrt(z):
    return com.sqrt(z)

def cthrt(z, **kwargs):
    opc = [k for k in kwargs]
    k = kwargs.get('k')
    if not 'k' in opc: k = 0
    if type(k) != int:
        sys.exit('No se ha introducido un valor de k adecuado.')
    return abs(z)**(1/3) * cexp(1j*(np.angle(z)+2*np.pi*k)/3)
    
def csin(z):
    return com.sin(z)

def ccos(z):
    return com.cos(z)
    
def carcsin(z):
    return com.asin(z)

def carccos(z):
    return com.acos(z)

def ctan(z):
    return com.tan(z)

def gamma(z):
    return sp.gamma(z)

def gamma2(z):
    return (sp.gamma(z) * sp.gamma(1-z))

def zetariemann(z):
    return zeta(z)


#Función compleja no analítica
def g6(z):
    return (z-(1-1j))*(z-(1+1j))*(z.conjugate()+1)**2