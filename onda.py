import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

res=300
anchoRendija=25
posRendija=int((2*res)/3)
xmin,xmax=0,30.0
ymin,ymax=0,30.0

tmin=0.0
tfinal=60.0

dx=30.0/res
dy=30.0/res
c=20
r=0.5

Nt=1000
dt=tfinal/Nt

e1=int(res/2)-anchoRendija
e2=int(res/2)+anchoRendija

matriz=np.zeros((Nt,res,res))
anchogota=2

matriz[0,int(res/3)-anchogota:int(res/3)+anchogota,int(res/2)-anchogota:int(res/2)+anchogota]=-0.5


matriz[1]=matriz[0]+r**2/2.*(np.roll(matriz[0],1,axis=0)+np.roll(matriz[0],-1,axis=0)+np.roll(matriz[0],1,axis=1)+np.roll(matriz[0],-1,axis=1)-4*matriz[0])

gR=2

#Bordes arriba, abajo
matriz[0,:,:gR],matriz[0,:,-gR:]=2,2
matriz[1,:,:gR],matriz[1,:,-gR:]=2,2
#Bordes lados izq, der
matriz[0,:gR,:],matriz[0,-gR:,:]=2,2
matriz[1,:gR,:],matriz[1,-gR:,:]=2,2
#Rendija


	 	
for t in range(2,Nt):
	#Solucion de ecuacion de onda
	matriz_0=matriz[t-2]
	matriz_1=matriz[t-1]
	matriz[t]=2*(1.-2.*r**2)*matriz_1-matriz_0+r**2*(np.roll(matriz_1,1,axis=1)+np.roll(matriz_1,-1,axis=1)+np.roll(matriz_1,1,axis=0)+np.roll(matriz_1,-1,axis=0))

	#Rendija
	matriz[t,:,:gR],matriz[t,:,-gR:]=2,2
	matriz[t,:gR,:],matriz[t,-gR:,:]=2,2
	matriz[t,posRendija-int(gR/2):posRendija+int(gR/2),:e1],matriz[t,posRendija-int(gR/2):posRendija+int(gR/2),e2:]=2,2

	#Fronteras de la rendija
	matriz[t,gR:-gR,-(gR+1)]=0
	matriz[t,gR,gR:-gR]=0
	matriz[t,-(gR+1),gR:-gR]=0
	matriz[t,gR+1:,gR]=0
	matriz[t,posRendija+int(gR/2),gR:e1]=0
	matriz[t,posRendija+int(gR/2),e2:-gR]=0
	matriz[t,posRendija-int(gR/2)-1,gR:e1]=0
	matriz[t,posRendija-int(gR/2)-1,e2:-gR]=0
	matriz[t,posRendija-int(gR/2)-1:posRendija+int(gR/2)+1,e2-1]=0
	matriz[t,posRendija-int(gR/2)-1:posRendija+int(gR/2)+1,e1]=0





from matplotlib import animation

plt.imshow(matriz[int(30*(Nt)/60)-1],extent=(xmin+dx,xmax-dx,ymin+dy,ymax-dy))
plt.title('Tiempo 30s')
plt.colorbar()
plt.savefig('t30.png')
plt.close()

plt.imshow(matriz[60*Nt/60-1],extent=(xmin+dx,xmax-dx,ymin+dy,ymax-dy))
plt.title('Tiempo 60s')
plt.colorbar()
plt.savefig('t60.png')
plt.close()

fig=plt.figure(figsize=(10,10))
plt.title('Animacion')
p=plt.imshow(matriz[0],cmap='bone',extent=(xmin+dx,xmax-dx,ymin+dy,ymax-dy))
plt.colorbar()

def animate(i):
	p.set_array((matriz[i]))
	return p,
animacion = animation.FuncAnimation(fig, animate, np.arange(1,len(matriz)),interval=5, blit=False)
animacion.save('Onda.mp4',fps=30,extra_args=['-vcodec', 'libx264'])

