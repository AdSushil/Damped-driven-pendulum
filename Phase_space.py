
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
a = 1.5 # chaotic amplitude. for different period orbit vary this with 1.35,1.45,1.47


#function that returns the DE as list.
def pend(y, t,q,a,w_d):
    o,x= y
    dydt = [x, -x/q -sin(o) + a*cos(w_d*t)]
    return dydt

# for intial conditon i.e angle and velocity of oscillation
y0 = [ 0, 0]
#y1 = [0.001,0]
#plotting phase space
t = np.linspace(0,200,10000)
sol = odeint(pend, y0, t, args=(q,a,w_d))
#sol1 = odeint(pend, y1, t, args=(q,a,w_d))
x_dot,o_dot = sol[0:, 1],sol[:, 0]
#x1,x2 = sol1[0:, 1],sol1[:, 0]

p = np.arctan2(np.sin(o_dot), np.cos(o_dot))
# this limits angle in range -pi to pi ..you can remove it directly plot the soln of DE.
#q = np.arctan2(np.sin(x2), np.cos(x2))
plt.scatter(p,x_dot,color='r',s=1,label=r'$\theta 1=0$')
#plt.scatter(q,x1,color='k',s=1,label=r'$\theta 2=0.001$')
plt.title('A = 1.5')
plt.legend(loc='upper right') 
plt.xlabel(r'$\theta$ (radian)')
plt.ylabel(r'$\omega$ (radian/sec)')
#plt.xlim(-3,3)
#plt.ylim(-2.5,1.5)
plt.grid(linestyle='--')
#plt.savefig('pp2150.png')
plt.show()
