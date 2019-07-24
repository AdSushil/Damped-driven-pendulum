from math import *
import matplotlib.pyplot as plt
from scipy import stats
from sklearn.linear_model import LinearRegression
plt.style.use('ggplot')
import numpy as np
g=1
l=1
D=2.0/3.0
q=0.5

class cp:
    def __init__(self,_theta=0.2,_w=0,_t=0,_dt=pi/1000):
        self.theta=[]
        self.theta.append(_theta)
        self.t=[]
        self.t.append(_t)
        self.w=[]
        self.w.append(_w)
        self.dt=_dt
    def cal(self,fd):
        global g,l,D,q,f1
        while(self.t[-1]<50):
            self.w.append(self.w[-1]-g/l*sin(self.theta[-1])*self.dt-q*self.w[-1]*self.dt+fd*cos(D*self.t[-1])*self.dt)
            self.theta.append(self.theta[-1]+self.w[-1]*self.dt)
            self.t.append(self.t[-1]+self.dt)
        
        return
    

#plot Lyapunov exponent

f_d = 1.47 # Driving amplitude
# here the slope of best fit gives the lyapunov exponent for each case
aa=cp(1.0) # first angle
bb=cp(1.001) # splt.savefig('p147.png')econd angle
aa.cal(f_d) #fd=1.2
bb.cal(f_d)  #fd  
d_theta=[]
for x1,x2 in zip(aa.theta,bb.theta):
    d_theta.append(abs(x1-x2))
x=[]
y=[]
for y1,y2 in zip(d_theta,aa.t):
    x.append(y2)
    y.append(y1)

# fitting for the lyapunov exponent

slope, intercept, r_value, p_value, std_err = stats.linregress(x,y)
line = [i*slope for i in x + intercept]

plt.xlabel('Time (sec)')
plt.ylabel(r'$\Delta\theta$ (radians)')
plt.semilogy(x,y,'r-')
plt.twinx()
equation = 'y='+str(round(slope,7))+'x'+ '+' +str(round(intercept,4))
plt.plot(x,line,'-',label=equation )
#xlim(0,50)

plt.legend(loc='lower right')
#plt.grid(linestyle='--')
plt.minorticks_on()
#plt.savefig('lp147.png')
plt.subplots_adjust(left=0.15)
plt.show()


