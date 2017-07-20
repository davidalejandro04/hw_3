import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import numpy.linalg as linalg
from mpl_toolkits.mplot3d import Axes3D
import mpl_toolkits.mplot3d.axes3d as p3
from matplotlib import animation
from datetime import datetime

t0 = datetime(1970,1,1, 0, 0)
ti = datetime(2017, 7, 20, 0, 0)
ti = (ti - t0).total_seconds()




a1=np.array(pd.read_csv('Datos.dat',header=None))
totaltiempos=int(len(a1)/10)
a2=np.zeros((int(totaltiempos*9.9),10,3))
for i in range(int(totaltiempos*9.9)):
	a2[i]=a1[i:i+10,1:4]

a2=a2[::50,:,:]


step=50

colors = ["yellow", "black", "purple", "blue", "red", "orange", "yellow", "cyan", "blue", "black"]
labels = ["Sol", "Mercurio", "Venus", "Tierra", "Marte", "Jupiter", "Saturno", "Urano", "Neptuno", "Pluton"]

fig = plt.figure()
ax = p3.Axes3D(fig)
plots = [ax.plot(a2[::step,i,0], a2[::step,i,1],a2[::step,i,2],label = labels[i], color = colors[i])[0] for i in range(10)]
ax.set_xlabel('$x$ $[AU]$')
ax.set_ylabel('$y$ $[AU]$')
ax.set_zlabel('$z$ $[AU]$')
plt.legend(loc=2)
plt.title(r'$ORBITAS$ $SISTEMA$ $SOLAR$')
plt.savefig('planetas.png')
plt.close()



fig = plt.figure()
ax = p3.Axes3D(fig)
text = ax.text(-40, -30, -10, "")
orbitasfijas = [ax.plot(a2[:, i, 0], a2[:, i, 1], a2[:, i, 2],c = colors[i]) for i in range(10)]
plots = [ax.plot([], [], [], "o",label = labels[i], color = colors[i],markersize=8)[0] for i in range(10)]
plots[0].set_marker("8")
plots[0].set_markersize(25)
ax.set_xlabel('$x$ $[AU]$')
ax.set_ylabel('$y$ $[AU]$')
ax.set_zlabel('$z$ $[AU]$')
plt.legend(loc=2)
plt.title(r'$ORBITAS$ $SISTEMA$ $SOLAR$')
plt.savefig('planetas.png')



def init():
	for (j, line) in enumerate(plots):
	        line.set_data([], [])
	        line.set_3d_properties([])
	text.set_text("")
	return plots, text

def update(i):
	for (j, line) in enumerate(plots):
	        line.set_data(a2[i, j, 0], a2[i, j, 1])
	        line.set_3d_properties(a2[i, j, 2])
	time = i*1/(365.25)*365.25*24*3600*len(a2)/float(len(a1)) + ti
	time = datetime.utcfromtimestamp(time)
	text.set_text(time.strftime('%Y-%m-%d'))
	return plots, text

animacion = animation.FuncAnimation(fig, update, len(a1))
#animacion.save("Bono-Planetas.mp4", fps = len(a2)/20,extra_args=['-vcodec', 'libx264'])

