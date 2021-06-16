######################
from Packages import *
######################

Dir=["d5004/HEADER","d5004/MRV","d5004/BAR"]
HeadMRV=["m", "rx" ,"ry" ,"rz","vx","vy","vz","itype"]
HeadBAR=["h","e","dn","t_star","f_g"]
convMass=1863506891.58 #Simulation Mass to MassSun

def convert(DataMRV,DataHead):
	G=6.67e-8
	Mpc=3.086e24
	H0=1e7/Mpc
	yr=3.16e7,
	kb=1.38e-16,
	mum=1.22*1.672649e-24,
	Msun=2e33

	tunit=DataHead['h0t0']/H0/DataHead['h100']
	box=DataHead['box100']/DataHead['h100']
	fl=DataHead['L']-2*DataHead['padding']
	lunit=box*Mpc/fl
	vunit=lunit/tunit
	eunit=vunit**2
	Kunit=(eunit*2.*mum)/3./kb
	convT=Kunit*(fl*DataHead['atime'])**2 
	#munit=(rhoc*Mpc)*(Mpc/Msun)*Mpc*box**3/rmtot*omega0
	DataMRV['Temperature']=convT.values*DataMRV['Temperature'].values
	#DataMRV.loc[:,'Temperature']=DataMRV['Temperature']*convT
	return(DataMRV)



def CreateDIR(DIR):
	try:
		os.mkdir(DIR)
	except FileExistsError:
		shutil.rmtree(DIR);
		os.mkdir(DIR);
	print('-> New folder created: {}\n'.format(DIR))


def ListData():
	snaps=[]
	root=[]

	for output in listdir("./d5004_mock/MRV/"):
		snaps.append(output)
		root.append('d5004_mock/MRV/'+output)
	snaps.sort()
	root.sort()
	return(snaps,root)


def Read_Save(Dir,root,name):

	datas=open(root,'rb')

	# |--------------Header--------------|
	dummy=[0 for x in range(100)]
	ibuf=[0 for x in range(100)]
	ibuf1=[0 for x in range(100)]
	ibuf2=[0 for x in range(100)]
	dummy2=[0 for x in range(100)]

	Data=[]


	for num in range(100):
		Buffer=datas.read(20)
		dummy[num], ibuf[num], ibuf1[num], ibuf2[num], dummy2[num]=(struct.unpack('>5i',Buffer)) 
		Buffer2=dummy[num], ibuf[num], ibuf1[num], ibuf2[num], dummy2[num]
		Data.append([])
		Data[num].extend(Buffer2)
	#np.save((Dir[0]+'/'+name),Data,allow_pickle=True,fix_imports=True)

	itime=ibuf1[0];	atime=(struct.unpack('>f', struct.pack('>i',ibuf1[5] )))
	atime=atime[0];	padding=(struct.unpack('>f', struct.pack('>i',ibuf1[19] )))
	padding=padding[0];	rmtot=(struct.unpack('>f', struct.pack('>i',ibuf1[32] )))
	rmtot=rmtot[0];	htime=(struct.unpack('>f', struct.pack('>i',ibuf1[6] )))
	htime=htime[0]	

	irun=ibuf2[0];nobj=ibuf2[1];ngas=ibuf2[2];ndark=ibuf2[3]
	L=ibuf2[4];	h100=struct.unpack('>f', struct.pack('>i',ibuf2[12] ))
	h100=h100[0];box100=struct.unpack('>f', struct.pack('>i',ibuf2[13] ))
	box100=box100[0];omega0=struct.unpack('>f', struct.pack('>i',ibuf2[21] ))
	omega0=omega0[0];xlambda0=struct.unpack('>f', struct.pack('>i',ibuf2[22] ))
	xlambda0=xlambda0[0];h0t0=struct.unpack('>f', struct.pack('>i',ibuf2[23] ))
	h0t0=h0t0[0]

	Values={'itime': itime, 'atime': atime, 'padding':padding , 'rmtot': rmtot,
		'irun':irun, 'nobj':nobj, 'ngas':ngas, 'ndark':ndark,'h100':h100,'box100': box100, 
		'omega0':omega0,'xlambda0':xlambda0, 'h0t0':h0t0, 'L':L, 'htime':htime}

	DataDF=pd.DataFrame(data=Values,index=[0])
	DataDF.to_csv((Dir[0]+'/'+name+'.csv'),header=True)



	
	del Data, Buffer2, dummy2, dummy, ibuf

	# |--------------MRV--------------|

	m=[0 for x in range(nobj)]
	rx=[0 for x in range(nobj)]
	ry=[0 for x in range(nobj)]
	rz=[0 for x in range(nobj)]
	vx=[0 for x in range(nobj)]
	vy=[0 for x in range(nobj)]
	vz=[0 for x in range(nobj)]
	itype=[0 for x in range(nobj)]
	Data=[]

	for num in range(nobj):
		Buffer=datas.read(40)
		dummy,m[num], rx[num], ry[num], rz[num],vx[num],vy[num],vz[num],itype[num],dummy2=(struct.unpack('>i7f2i',Buffer))
		Buffer2=m[num], rx[num], ry[num], rz[num],vx[num],vy[num],vz[num],itype[num]
		Data.append([])
		Data[num].extend(Buffer2)
	np.save((Dir[1]+'/'+name),Data,allow_pickle=True,fix_imports=True)
	del Data, Buffer2

	# |--------------BAR--------------|


	h=[0 for x in range(nobj-ndark)]
	e=[0 for x in range(nobj-ndark)]
	dn=[0 for x in range(nobj-ndark)]
	t_star=[0 for x in range(nobj-ndark)]
	f_g=[0 for x in range(nobj-ndark)]
	Data=[]

	for num in range((nobj-ndark)):
		Buffer=datas.read(28)
		dummy,h[num],e[num],dn[num],t_star[num],f_g[num], dummy2=(struct.unpack('>i5fi',Buffer))
		Buffer2=h[num],e[num],dn[num],t_star[num],f_g[num]
		Data.append([])
		Data[num].extend(Buffer2)
	np.save((Dir[2]+'/'+name),Data,allow_pickle=True,fix_imports=True)
	del Data, Buffer2

	datas.close()
