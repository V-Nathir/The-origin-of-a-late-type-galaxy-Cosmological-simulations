import numpy as np
import matplotlib.pyplot as plt
from random import randint
from random import choice
import random
from os import listdir
m= []
rx =[]
ry = []
rz = []
vx =[]
vy = []
vz = []
itype = []
random.seed(1444450)
def ListData2():
	snaps=[]
	root=[]

	for output in listdir("./d5004_mock/MRV"):
		snaps.append(output)
		root.append(output[:-4])
	snaps.sort()
	root.sort()
	return(snaps,root)
snaps,root=ListData2()


for i in range(500000):
	m.append(randint(0,5)*randint(0,5))
	rx.append(randint(0,5)*randint(0,5))
	ry.append(randint(0,5)*randint(0,5))
	rz.append(randint(0,5)*randint(0,5))
	vx.append(randint(0,10)*randint(1,5))
	vy.append(randint(0,10)*randint(1,5))
	vz.append(randint(0,10)*randint(1,5))
	itype.append( choice([-1, 1]))

m  = np.array(m)/100
plt.hist(m)
plt.show()
rx  = np.array(rx)/100
ry  = np.array(ry)/100
rz  = np.array(rz)/100
vx  = np.array(vx)/10
vy  = np.array(vy)/10
vz  = np.array(vz)/10
itype  = np.array(itype)
data = np.zeros((500000, 8))
data[:,0] = m
data[:,1] = rx
data[:,2] = ry
data[:,3] = rz
data[:,4] = vx
Cerovelx = data[:,4]
Cerovely = data[:,5]
data[:,5] = vy
data[:,6] = vz
data[:,7] = itype

np.save(('d5004_mock/MRV/'+snaps[0]),data,allow_pickle=True,fix_imports=True)

theta = np.linspace(0,10*np.pi,len(snaps))


for i,j in zip(snaps,theta): 
	data[:,1] = data[:,1]-randint(0,3)*0.11*data[:,1]
	#plt.hist(data[:,1]); plt.show()
	data[:,2] = data[:,2]-randint(0,3)*0.11*data[:,2]
	data[:,3] = data[:,3]-randint(0,3)*0.11*data[:,3]
	data[:,4] = data[:,4]- np.sin(j)*Cerovelx
	data[:,5] = data[:,5]- np.sin(10*np.pi-j)*Cerovely
	
	indice = np.where(data[:,7]==1. )[0]
	lon = len(indice)
	indice = indice[0: int(np.floor(lon/5)) ]
	for k in indice: 
		data[k,7] = choice([-1, 1])

	np.save(('d5004_mock/MRV/'+i),data,allow_pickle=True,fix_imports=True)
HeadMRV=["m", "rx" ,"ry" ,"rz","vx","vy","vz","itype"]
m= []
rx =[]
ry = []
rz = []
vx =[]
vy = []
vz = []
itype = []
random.seed(3000)
def ListData2():
	snaps=[]
	root=[]

	for output in listdir("./d5004_mock/MRV"):
		snaps.append(output)
		root.append(output[:-4])
	snaps.sort()
	root.sort()
	return(snaps,root)
snaps,root=ListData2()

"""
for i in range(1000000):
	m.append(randint(5,10)*randint(1,5))
	rx.append(randint(0,10)*randint(1,5))
	ry.append(randint(0,10)*randint(1,5))
	rz.append(randint(0,10)*randint(1,5))
	vx.append(randint(0,5)*randint(1,5))
	vy.append(randint(0,5)*randint(1,5))
	vz.append(randint(0,5)*randint(1,5))
	itype.append( choice([-1, 1]))
m  = np.array(m)/50
rx  = np.array(rx)/50
ry  = np.array(ry)/50
rz  = np.array(rz)/50
vx  = np.array(vx)/50
vy  = np.array(vy)/50
vz  = np.array(vz)/50
itype  = np.array(itype)
data = np.zeros((10000, 8))
data[:,0] = m
data[:,1] = rx
data[:,2] = ry
data[:,3] = rz
data[:,4] = vx
Cerovelx = data[:,4]
Cerovely = data[:,5]
data[:,5] = vy
data[:,6] = vz
data[:,7] = itype

np.save(('CW/Data/'+snaps[0]),data,allow_pickle=True,fix_imports=True)

theta = np.linspace(0,10*np.pi,len(snaps))


for i,j in zip(snaps,theta): 
	data[:,1] = data[:,1]-0.15*data[:,1]
	data[:,2] = data[:,2]-0.15*data[:,2]
	data[:,3] = data[:,3]-0.15*data[:,3]
	data[:,4] = data[:,4]- np.sin(j)*Cerovelx
	data[:,5] = data[:,5]- np.sin(10*np.pi-j)*Cerovely
	
	indice = np.where(data[:,7]==1. )[0]
	lon = len(indice)
	indice = indice[0: int(np.floor(lon/5)) ]
	for k in indice: 
		data[k,7] = choice([-1, 1])

	np.save(('CW/data/'+i),data,allow_pickle=True,fix_imports=True)


"""






















