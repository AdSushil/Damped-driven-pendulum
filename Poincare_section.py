from scipy.integrate import odeint
import numpy as np
from numpy import sin,pi,cos
import matplotlib.pyplot as plt
plt.style.use('ggplot')
# DE is o'' = -(b/I)*o' - (mlg/I)*sino + (A/I)cos(w_d*t)
# suppose o'=x , x' = -b*x - g/l*sino
# constant values
q = 2.0
w_d = 2.0/3.0
a = 1.5
# this is chaotic case you can vary it for  1.35, 1.45, 1.47 for periodic case.

#function that returns the DE as list.
def pend(y, t,q,a,w_d):
    o,x= y
    dydt = [x, -x/q -sin(o) + a*cos(w_d*t)]
    return dydt

# for intial conditon i.e angle and velocity of oscillation
y0 = [ 0, 0]

#plot poincare space
p = (pi)/w_d
n= 5000
T= n*p  #p=2pi/w_d
h=p/n   #step size
t = np.arange(0,T,h) 
xs = odeint(pend, y0, t,args=(q,a,w_d))
x1 = [xs[n*i, 0] for i in range(n)]
x =  map(lambda x: x, x1)
z=  np.arctan2(sin(x), cos(x)) # change angle in range -pi to pi
y = [xs[n*j, 1] for j in range(n)]  
plt.scatter(z, y, color='red',s=0.5,label="A=1.5")
plt.xlabel(r'$\theta$ (radian)')
plt.ylabel(r'$\omega$ (radian/sec)')
plt.legend(loc='best')
plt.title('The Poincare section')
#plt.grid(linestyle='--')
#plt.savefig('pp150.png')

plt.show()
