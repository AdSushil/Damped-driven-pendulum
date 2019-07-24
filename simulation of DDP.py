import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import matplotlib as mpl
plt.style.use('ggplot')
# Constants 
g = 1       # acceleration due to gravity (m/s^2)
m = 1       # mass attached to rod (kg)
L = 1       # length of the rod (m)
F = 0.2     # forced force amplitude (N)
w = 2.0/3.0      # damping coefficient
I = m*L**2  # moment of inertia (kg*m^2)
w0 = np.sqrt(g/L)  # resonance frequency (s^-1)
q = 2.0
a = 1.5


# Plot and animation parameters
dt = 0.01
t = np.arange(0.0, 30, dt)  # time steps
th1 = 0.0  # initial angle in radians
a1 = 0.0   # initial angular velocity in radian per second
init_state = [th1, a1]  # [theta, dth_dt]

#wmin = w0-2
#wmax = w0+2
#dw = 0.1
#ws = np.arange(wmin, wmax, dw)  # forcing frequencies (< w0)


def deriv(state, t, w):
    """Return [dtheta_dt, d2theta_dt2].
    For use with odeint.
    """
    global g, m, L, F, I,q,a
    theta = state[0]
    dth_dt = state[1]
    return [dth_dt, -dth_dt/q - w0*np.sin(theta) + a*np.cos(w*t)]


# Animation of the pendulum with w=w0 (pendulum.mp4)
fig2 = plt.figure(2)
ax2 = fig2.add_subplot(111, autoscale_on=False, xlim=(-2, 2), ylim=(-2, 2))
line, = ax2.plot([], [], 'o-',color='r',lw=2,label='A=1.5')
time_template = 'Time = %.1fs'
time_text = ax2.text(0.05, 0.9, '', transform=ax2.transAxes)

yM = odeint(deriv, init_state, t, args=(w0,))
xs = L * np.sin(yM[:, 0])
ys = -L * np.cos(yM[:, 0])


def init():
    line.set_data([], [])
    time_text.set_text('')
    return line, time_text


def updatefig(i):
    thisx = [0, xs[i]]
    thisy = [0, ys[i]]

    line.set_data(thisx, thisy)
    time_text.set_text(time_template % (i*dt))
    return line, time_text


ani = animation.FuncAnimation(fig2, updatefig, range(len(xs)), interval=10, blit=True, init_func=init)

plt.legend(loc='best') 
#plt.grid(linestyle='--')
#plt.twinx()
plt.show()
