from Packages import * 

def signatura(v1,v2,column):
	signos=np.sign(np.array(v1[:,column]))
	signo_snap=np.sign(np.array(v2[:,column]))
	
	if signos[0]!=signo_snap[0]:
		 v2[0,column]=v2[0,column]*-1
	if signos[1]!=signo_snap[1]:
		 v2[1,column]=v2[1,column]*-1
	if signos[2]!=signo_snap[2]:
		 v2[2,column]=v2[2,column]*-1
	return(v2)

def signatura_cross(v1,v2,column1,column2):
	signos=np.sign(np.array(v1[:,column1]))
	signo_snap=np.sign(np.array(v2[:,column2]))
	
	if signos[0]!=signo_snap[0]:
		 v2[0,column2]=v2[0,column2]*-1
	if signos[1]!=signo_snap[1]:
		 v2[1,column2]=v2[1,column2]*-1
	if signos[2]!=signo_snap[2]:
		 v2[2,column2]=v2[2,column2]*-1
	return(v2)

def SupportIT_e3(last_eigenvector,prelast_evec,eigenvectors,eigenvalues,mode='none'):
	e1_b=last_eigenvector[:,0]; e2_b=last_eigenvector[:,1]; e3_b=(last_eigenvector[:,2])
	e1_pb=prelast_evec[:,0]; e2_pb=prelast_evec[:,1]; e3_pb=(prelast_evec[:,2])
	e1=eigenvectors[:,0]; e2= eigenvectors[:,1]; e3=eigenvectors[:,2]; 

	pcosA=(np.dot(e1,e1_pb)); pcosA2=(np.dot(e2,e2_pb)); pcosA3=(np.dot(e3,e3_pb)) # con la anteior
	cose3      = np.abs(np.dot(e3,e3_pb)); cos1=np.abs(np.dot(e1,e1_pb))
	cose3_inv1 = np.abs(np.dot(e1,e3_pb)); cos2=np.abs(np.dot(e2,e2_pb))
	cose3_inv2 = np.abs(np.dot(e2,e3_pb));

	if mode=='none':
		chk='no'
		if cose3<cose3_inv2 and cose3_inv2>cose3_inv1:
			eigenvalues=np.array([eigenvalues[0],eigenvalues[2],eigenvalues[1]])
			eigenvectors=np.array([[e1[0],e3[0],e2[0]],[e1[1],e3[1],e2[1]],[e1[2],e3[2],e2[2]]])
			chk= 'yes'
		e1=eigenvectors[:,0]; e2= eigenvectors[:,1]; e3=eigenvectors[:,2]; 
		pcosA3=(np.dot(e3,e3_pb))
		if cose3<cose3_inv1 and chk=='no' and  cose3_inv1>cose3_inv2:
			eigenvalues=np.array([eigenvalues[2],eigenvalues[1],eigenvalues[0]])
			eigenvectors=np.array([[e3[0],e2[0],e1[0]],[e3[1],e2[1],e1[1]],[e3[2],e2[2],e1[2]]])
		e1=eigenvectors[:,0]; e2= eigenvectors[:,1]; e3=eigenvectors[:,2]; 
		pcosA3=(np.dot(e3,e3_pb))
		
		if pcosA3<=-0.99:
			eigenvectors=signatura(prelast_evec,eigenvectors,2)
		
		
	#Corrección de los autovectorer medianos y menores
	if mode=='sph':
		
		test_e1=signatura_cross(prelast_evec,eigenvectors,2,0);test_cos=np.abs(np.dot(test_e1[:,0],e3_pb))
		if cose3<cose3_inv2 and cose3_inv2>cose3_inv1:
			eigenvalues=np.array([eigenvalues[0],eigenvalues[2],eigenvalues[1]])
			eigenvectors=np.array([[e1[0],e3[0],e2[0]],[e1[1],e3[1],e2[1]],[e1[2],e3[2],e2[2]]])
		e1=eigenvectors[:,0]; e2= eigenvectors[:,1]; e3=eigenvectors[:,2]; 
		cose3 = np.abs(np.dot(e3,e3_pb)); cose3_inv1 = np.abs(np.dot(e1,e3_pb));cose3_inv2 = np.abs(np.dot(e2,e3_pb));
		if cose3<cose3_inv1 and cose3_inv1>cose3_inv2:
			eigenvalues=np.array([eigenvalues[2],eigenvalues[1],eigenvalues[0]])
			eigenvectors=np.array([[e3[0],e2[0],e1[0]],[e3[1],e2[1],e1[1]],[e3[2],e2[2],e1[2]]])
		e1=eigenvectors[:,0]; e2= eigenvectors[:,1]; e3=eigenvectors[:,2]; 
		pcosA3=(np.dot(e3,e3_pb))
		
		if pcosA3<=-0.99:
			eigenvectors=signatura(prelast_evec,eigenvectors,2)

	return(eigenvalues,eigenvectors)


def SupportIT_e1(last_eigenvector,prelast_evec,eigenvectors,eigenvalues):
	e1_b=last_eigenvector[:,0]; e2_b=last_eigenvector[:,1]; e3_b=(last_eigenvector[:,2])
	e1_pb=prelast_evec[:,0]; e2_pb=prelast_evec[:,1]; e3_pb=(prelast_evec[:,2])
	e1=eigenvectors[:,0]; e2= eigenvectors[:,1]; e3=eigenvectors[:,2]

	pcosA=(np.dot(e1,e1_pb)); pcosA2=(np.dot(e2,e2_pb)); pcosA3=(np.dot(e3,e3_pb)) # con la anteior
	cose12=np.abs(np.dot(e3,e2_pb)); cos1=np.abs(np.dot(e3,e3_pb)) #!!!!!!!
	cose21=np.abs(np.dot(e2,e3_pb)); cos2=np.abs(np.dot(e2,e2_pb))

	

	#Corrección de los autovectorer medianos y mayor
	
	if cos1<cose12 and cos2<cose21:
		eigenvalues=np.array([eigenvalues[0],eigenvalues[2],eigenvalues[1]])
		eigenvectors=np.array([[e1[0],e3[0],e2[0]],[e1[1],e3[1],e2[1]],[e1[2],e3[2],e2[2]]])
	
	if pcosA<=-0.9:
		eigenvectors=signatura(prelast_evec,eigenvectors,0)

	return(eigenvalues,eigenvectors)

def InertiaTensor(data,CM,snap,last_eigenvector,prelast_evec,initial,estable,mode='none',fixeigenval='no'):
	#LAST_EIGENVECTOR  (Z=0)
	x=data['rx']-CM[snap,0];y=data['ry']-CM[snap,1];z=data['rz']-CM[snap,2]

	Ixx=data['m']*(y**2+z**2)/(x**2+y**2+z**2); Ixx=Ixx.sum()
	Iyy=data['m']*(x**2+z**2)/(x**2+y**2+z**2); Iyy=Iyy.sum()
	Izz=data['m']*(x**2+y**2)/(x**2+y**2+z**2); Izz=Izz.sum()
	Ixy=-data['m']*(x*y)/(x**2+y**2+z**2);Ixy=Ixy.sum()
	Ixz=-data['m']*(x*z)/(x**2+y**2+z**2);Ixz=Ixz.sum()
	Izy=-data['m']*(y*z)/(x**2+y**2+z**2);Izy=Izy.sum()

	I=np.array([[Ixx,Ixy,Ixz],[Ixy,Iyy,Izy],[Ixz,Izy,Izz]])

	eigenvalues,eigenvectors=np.linalg.eig(I)
	idx = eigenvalues.argsort()[::1]   
	eigenvalues = eigenvalues[idx]
	eigenvectors = eigenvectors[:,idx]; 
	


	if initial=='no':
		if fixeigenval =='yes':
			if estable==3:
				#e3 stable eigenvector
				eigenvalues,eigenvectors=SupportIT_e3(last_eigenvector,prelast_evec,eigenvectors,eigenvalues,mode)
			
			if estable==1:
				#e1 stable eigenvector
				eigenvalues,eigenvectors=SupportIT_e1(last_eigenvector,prelast_evec,eigenvectors,eigenvalues)
		
		
		return(I,eigenvalues,eigenvectors)

	else:

		return(I,eigenvalues,eigenvectors)


def MinorAxis(eigenvalues,data):
	a=np.sqrt(5*(eigenvalues[1]-eigenvalues[0]+eigenvalues[2])/(2*data['m'].sum()) )
	b=np.sqrt(5*(eigenvalues[2]-eigenvalues[1]+eigenvalues[0])/(2*data['m'].sum()) )
	c=np.sqrt(5*(eigenvalues[0]-eigenvalues[2]+eigenvalues[1])/(2*data['m'].sum()) )
	axis=[a,b,c]
	return(axis)

def Deformation(a,b,c):
	T=(1-b**2/a**2)/(1-c**2/a**2)
	e=(a**2-c**2)/(a**2+b**2+c**2)
	p=(a**2+c**2-2*b**2)/(a**2+b**2+c**2)
	return(T,e,p)

def Aitoff(Vector_EValue):

	x=Vector_EValue[0]
	y=Vector_EValue[1]
	z=Vector_EValue[2]

	if z >=0:
		DEC=(np.pi/2-np.arctan(np.sqrt(x**2+y**2)/z) )
	if z<0:
		DEC=(-np.pi/2-np.arctan(np.sqrt(x**2+y**2)/z) )
	if y>=0 and x>=0:
		AR=np.arctan(y/x)

	if y<0 and x>=0:
		AR=np.arctan(y/x)

	if x<0:
		AR=np.pi+np.arctan(y/x)
		if AR>np.pi:
			AR=AR-2*np.pi
	if DEC<0:
		if AR<0:
			AR=(AR)+np.pi
		if AR>0:
			AR=(AR)-np.pi
		DEC=np.absolute(DEC)
	if AR<0:
		AR=AR+np.pi
	return(AR,DEC)

def AitoffProjection(Vector,snaps,Subplot,name,estable):
	if estable==3:
		evector=2
	if estable==1:
		evector=0

	plt.subplot(Subplot, projection="aitoff")
	Progress = ChargingBar('Plotting the Aitoff proyection '+str(Subplot)+':', max=len(snaps))
	colors = cm.rainbow(np.linspace(0, 1, 61))
	for i,j in zip(snaps,range(len(snaps))):
		AR,DEC=Aitoff(Vector[i][:,evector]);c=[colors[j]]
		plt.scatter(AR,DEC,color=c,marker='o',s=12)
	plt.title(name,fontsize=20)
	plt.grid(True)
	Progress.finish()

def PlotOneAxis(case,axis1,label1,c1,axis2,label2,c2,axis3,label3,c3,axis4,label4,c4,redshift):
	longit=np.round(np.linspace(0,60,61))
	R=plt.figure(figsize=(13.0, 10.0))
	ax=R.add_subplot(111)
	ax.plot(longit,axis1,linestyle='--',marker='o',color=c1,markersize=4,label=label1)
	ax.plot(longit,axis2,linestyle='--',marker='o',color=c2,markersize=4,label=label2)
	ax.plot(longit,axis3,linestyle='--',marker='o',color=c3,markersize=4,label=label3)
	ax.plot(longit,axis4,linestyle='--',marker='o',color=c4,markersize=4,label=label4)

	plt.xticks(longit,redshift);plt.xticks(rotation=90)
	ax.set_ylabel('Values of minor axis '+ case,fontsize=20);ax.set_xlabel('Redshift',fontsize=20)
	ax.set_title('The changes of the axis values: '+ case,fontsize=20)
	plt.legend(shadow=True)
	plt.grid(True)
	plt.savefig('CentralGalaxy/Plots/Axis/'+case+'.pdf', bbox_inches = 'tight')
	plt.close()

def PlotMinorAxis(case,axisname,axis1,label1,c1a,c1b,c1c,axis2,label2,c2a,c2b,c2c,redshift):
	longit=np.round(np.linspace(0,60,61))
	R=plt.figure(figsize=(13.0, 10.0))
	ax=R.add_subplot(111)
	ax.plot(longit,axis1[:,2],linestyle='--',marker='o',color=c1a,markersize=4) #a
	ax.plot(longit,axis1[:,1],linestyle='--',marker='o',color=c1b,markersize=4)
	ax.plot(longit,axis1[:,0],linestyle='--',marker='o',color=c1c,markersize=4)

	ax.plot(longit,axis2[:,2],linestyle='--',marker='o',color=c2a,markersize=4)
	ax.plot(longit,axis2[:,1],linestyle='--',marker='o',color=c2b,markersize=4)
	ax.plot(longit,axis2[:,0],linestyle='--',marker='o',color=c2c,markersize=4)
	
	ax.plot([],[],marker='o',color=c1a,label=label1)
	ax.plot([],[],marker='o',color=c1b,label='b')
	ax.plot([],[],marker='o',color=c1c,label='c')

	ax.plot([],[],marker='o',color=c2a,label=label2)
	ax.plot([],[],marker='o',color=c2b,label='b')
	ax.plot([],[],marker='o',color=c2c,label='c')

	plt.xticks(longit,np.round(redshift,3));plt.xticks(rotation=90)
	ax.set_ylabel('Values of minor axis '+ axisname,fontsize=20);ax.set_xlabel('Redshift',fontsize=20)
	ax.set_title('The changes of the axis values: '+ case,fontsize=20)
	plt.legend(shadow=True)
	plt.grid(True)
	plt.savefig('CentralGalaxy/Plots/Axis/'+axisname+'_'+case+'.pdf', bbox_inches = 'tight')
	plt.close()
