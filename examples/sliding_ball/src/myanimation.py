# python_exercises/pexercise2/myanimation.py

import matplotlib.pyplot as plt
from math import sin, cos, pi
import numpy as np
from matplotlib import animation

def animatePendulum(theta, t, l=1):
            
    # set up figure and animation
    
    fig = plt.figure()
    ax = fig.add_subplot(111, aspect='equal', autoscale_on=False,
                         xlim=(-1.1, 1.1), ylim=(-1.1, 1.1))
    #ax.grid()
    theta_line = np.linspace(0, pi, 101)
    line, = ax.plot([], [], 'o', lw=5)
    line2, = ax.plot(-l*np.cos(theta_line), -l*np.sin(theta_line), 'k-', lw=1)
    time_text = ax.text(0.02, 0.95, '', transform=ax.transAxes)
    theta_text =  ax.text(0.02, 0.85, '', transform=ax.transAxes)
    def init():
        """initialize animation"""
        line.set_data([], [])
        time_text.set_text('')
        theta_text.set_text('')
        return line, time_text
    
    def animate(i):
        """perform animation step"""
        x = -l*cos(theta[i])
        y = -l*sin(theta[i])
        deg = theta[i]*180/pi
        
        line.set_data([x], [y])
        time_text.set_text('time = %.1f [-]' % t[i])
        theta_text.set_text(r'$\theta$ = %.0f $^o$' % deg)
        return line2, line, time_text
    
    # choose the interval based on dt and the time to animate one step
    Npictures = len(t)
    ani = animation.FuncAnimation(fig, animate,init_func=init,frames=Npictures,interval=1,blit=False)
    

    #Writer = animation.writers['ffmpeg']
    #writer = Writer(fps=15, metadata=dict(artist='Me'), bitrate=1800)
    #ani.save('pendulum.mov', writer=writer)
    
    plt.show()