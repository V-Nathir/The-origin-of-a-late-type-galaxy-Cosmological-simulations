##############################
from Packages import *
from Def_ReadAndSave import convert
from PostCM_V3 import *
##############################

def Table(titles, rows):
	TABLE=PrettyTable()
	TABLE.field_names=titles
	for r in range(len(rows[:])):
		TABLE.add_row(rows[r])
	print(TABLE);print('\n')

def magnitude(vector):  
	return( (float(vector[0]**2+vector[1]**2+vector[2]**2 ))**(1/2))

def Selection(DATA,particlesID,Dir,snap,head,SAVE='no'):
	
	DataDF=pd.DataFrame(DATA[snap][particlesID-1,:],columns=head);	DataDF.insert(0,"ID",particlesID,True)
	if SAVE=="yes":
		DataDF.to_csv((Dir+'/'+snap+'.csv'),header=True, index=False)
	#np.save(('Particles_CentralGalaxy/'+i),DATA,allow_pickle=True,fix_imports=True)

	return(DataDF)
	
def Cal_MassCenter(DataFrame):
	try:
		buf_matter=DataFrame['m'].sum()
		
		buf_rx=DataFrame['m']*DataFrame['rx']
		buf_rx=buf_rx.sum()/buf_matter

		buf_ry=DataFrame['m']*DataFrame['ry']
		buf_ry=buf_ry.sum()/buf_matter

		buf_rz=DataFrame['m']*DataFrame['rz']
		buf_rz=buf_rz.sum()/buf_matter
	except RuntimeWarning:
		buf_rx=0 ; buf_ry=0 ; buf_rz= 0
		
	CM=np.array([buf_rx,buf_ry,buf_rz]);
	return(CM)

def MassCenter2(Snaps_DataDF,snap,scale,r_PostCM,r_sub,CMZ):
	if isinstance(CMZ,str):
		CM0=Cal_MassCenter(Snaps_DataDF[snap]) ;CM0_reser=CM0
	else:
		CM0=CMZ ; CM0_reser = CMZ

	radius=radius_particle(Snaps_DataDF,snap,CM0)
	tol_var=radius.max() ; tol_fix=radius.max()
	maxParts = len(Snaps_DataDF[snap])

	if scale =='LSS':
		tolfixed_cm=0.00099
		percent=0.05
		tol_var=tol_var-tol_fix*percent*4
		cantidad_particulas=maxParts
		radiuscm0_fix= 0; buf_deltar = 1000

	if scale == 'galaxy':
		tolfixed_cm=0.000099
		percent=0.01
		tol_var=tol_var-tol_fix*percent
		part_percent = 0.1 ; 
		cantidad_particulas = maxParts*part_percent ; 
		radiuscm0_fix=np.sqrt(CM0[0]**2+CM0[1]**2+CM0[2]**2)
		buf_deltar = 0.01


	#print('Máximo radio {} y tol dada {}'.format(tol_fix,tol_var))
	particles_ker=[]; particles_del=[]; 
	global_buf=True
	nbucle = 0
	while global_buf==True :
		if tol_var<0:
			if scale =='LSS':
				tolfixed_cm=0.00099
			if scale == 'galaxy':
				tolfixed_cm=tolfixed_cm
				nbucle = nbucle + 1 
				if nbucle == 2:
					nbucle=0
					part_percent = part_percent + 0.2
					if part_percent >1:
						part_percent=1
					cantidad_particulas = np.ceil(maxParts*part_percent)

			tol_var=tol_fix; percent=percent*0.75
			tol_var=tol_var-tol_fix*percent
			CM0=CM0_reser ; 
		radius=radius_particle(Snaps_DataDF,snap,CM0)
		particles_ker=Snaps_DataDF[snap][radius<tol_var]
		particles_del=Snaps_DataDF[snap][radius>tol_var]
		#----------New CM--------
		CM=Cal_MassCenter(particles_ker)
		
		radiuscm=np.sqrt(CM[0]**2+CM[1]**2+CM[2]**2)
		radiuscm0=np.sqrt(CM0[0]**2+CM0[1]**2+CM0[2]**2)

		if np.absolute(radiuscm-radiuscm0)<tolfixed_cm:
			tol_var2=tol_var-tol_fix*percent*2
			#print('tol_var2 dentro de global {}'.format(tol_var2))
			particles_ker2=Snaps_DataDF[snap][radius<tol_var2]
			particles_del2=Snaps_DataDF[snap][radius>tol_var2]

			CM2=Cal_MassCenter(particles_ker2)
		
			radiuscm=np.sqrt(CM[0]**2+CM[1]**2+CM[2]**2)
			radiuscm2=np.sqrt(CM2[0]**2+CM2[1]**2+CM2[2]**2)
			cantidad_particulasin = len(particles_ker)
			if  np.absolute(radiuscm-radiuscm2)<tolfixed_cm and cantidad_particulasin <= cantidad_particulas and cantidad_particulasin>=200:
				#np.absolute(radiuscm-radiuscm0_fix)<=buf_deltar
				global_buf=False
			else:
				tol_var=tol_var-tol_fix*percent
		else:
			tol_var=tol_var-tol_fix*percent
			CM0=CM
	Snaps_DataDF[snap].insert(8,"radius",radius,True)
	#print('Particulas in out : {}  - {} '.format(len(particles_ker),len(particles_del) ))
	#print(CM)
	"""
	if scale=='galaxy':
		print('Radio max desde el CM previo {} ampliado a {}'.format(max(radius), max(radius)+max(radius)*0.25 ))
		maxr_partin = max(radius) 
		print('Radio par encontrar la sobredensdiad {}'.format(r_PostCM))
		print('Radio entorno a la particula {}'.format(r_sub))
		CM=PostCM(Snaps_DataDF,snap,CM,r_PostCM,r_sub,maxr_partin)
	"""
	#print(CM)
	return(CM[0],CM[1],CM[2],particles_ker,particles_del,len(particles_ker['m']),len(particles_del['m']))


def MassCenter(Snaps_DataDF,snap,scale,r_PostCM,r_sub):

	CM0=Cal_MassCenter(Snaps_DataDF[snap]) ;CM0_reser=CM0
	radius=radius_particle(Snaps_DataDF,snap,CM0)
	tol_var=radius.max() ; tol_fix=radius.max()
	maxParts = len(Snaps_DataDF[snap])

	if scale =='LSS':
		tolfixed_cm=0.00099
		percent=0.05
		tol_var=tol_var-tol_fix*percent*4
		cantidad_particulas=maxParts/2

	if scale == 'galaxy':
		tolfixed_cm=0.000099
		percent=0.01
		tol_var=tol_var-tol_fix*percent
		part_percent = 0.1 ; 
		cantidad_particulas = maxParts*part_percent ; 


	#print('Máximo radio {} y tol dada {}'.format(tol_fix,tol_var))
	particles_ker=[]; particles_del=[]; 
	global_buf=True
	nbucle = 0
	while global_buf==True :
		if tol_var<0:
			nbucle = nbucle + 1 
			if scale =='LSS':
				tolfixed_cm=0.00099
				if nbucle == 3: 
					nbucle=0
					cantidad_particulas=maxParts

			if scale == 'galaxy':
				tolfixed_cm=tolfixed_cm
				if nbucle == 2:
					nbucle=0
					part_percent = part_percent + 0.2
					if part_percent >1:
						part_percent=1
					cantidad_particulas = np.ceil(maxParts*part_percent)

			tol_var=tol_fix; percent=percent*0.75
			tol_var=tol_var-tol_fix*percent
			CM0=CM0_reser ; 
		radius=radius_particle(Snaps_DataDF,snap,CM0)
		particles_ker=Snaps_DataDF[snap][radius<tol_var]
		particles_del=Snaps_DataDF[snap][radius>tol_var]
		#----------New CM--------
		CM=Cal_MassCenter(particles_ker)
		
		radiuscm=np.sqrt(CM[0]**2+CM[1]**2+CM[2]**2)
		radiuscm0=np.sqrt(CM0[0]**2+CM0[1]**2+CM0[2]**2)

		if np.absolute(radiuscm-radiuscm0)<tolfixed_cm:
			tol_var2=tol_var-tol_fix*percent*2
			#print('tol_var2 dentro de global {}'.format(tol_var2))
			particles_ker2=Snaps_DataDF[snap][radius<tol_var2]
			particles_del2=Snaps_DataDF[snap][radius>tol_var2]

			CM2=Cal_MassCenter(particles_ker2)
		
			radiuscm=np.sqrt(CM[0]**2+CM[1]**2+CM[2]**2)
			radiuscm2=np.sqrt(CM2[0]**2+CM2[1]**2+CM2[2]**2)
			cantidad_particulasin = len(particles_ker)
			if np.absolute(radiuscm-radiuscm2)<tolfixed_cm and cantidad_particulasin <= cantidad_particulas and cantidad_particulasin>=200:
				global_buf=False
			else:
				tol_var=tol_var-tol_fix*percent
		else:
			tol_var=tol_var-tol_fix*percent
			CM0=CM
	Snaps_DataDF[snap].insert(8,"radius",radius,True)
	#print('Particulas in out : {}  - {} '.format(len(particles_ker),len(particles_del) ))
	#print(CM)
	"""
	if scale=='galaxy':
		print('Radio max desde el CM previo {} ampliado a {}'.format(max(radius), max(radius)+max(radius)*0.25 ))
		maxr_partin = max(radius) 
		print('Radio par encontrar la sobredensdiad {}'.format(r_PostCM))
		print('Radio entorno a la particula {}'.format(r_sub))
		CM=PostCM(Snaps_DataDF,snap,CM,r_PostCM,r_sub,maxr_partin)
	"""
	#print(CM)
	return(CM[0],CM[1],CM[2],particles_ker,particles_del,len(particles_ker['m']),len(particles_del['m']))

def CMdistance(Datos,CM,snaps,redshift,types,name):
	R=plt.figure(figsize=(13.0, 10.0))
	ax=R.add_subplot(111)
	names=['Disk','Spheroid']
	color=['blue','red']
	longit=np.round(np.linspace(0,len(snaps)-1,len(snaps)))

	Disk_std=[];Sph_std=[]
	for T,t in zip(types,range(2)):
		for s,z in zip(snaps,range(len(snaps))):
			if T==1:
				Buf=Datos[s].loc[(Datos[s]['Component']==T) | (Datos[s]['Component']==T+1) ]
			else: 
				Buf=Datos[s].loc[Datos[s]['Component']==T]
			Mod=np.array(Buf['rx'].values**2+Buf['ry'].values**2+Buf['rz'].values**2)

			distance=np.absolute( np.sqrt(Mod)-np.sqrt(CM[z,0]**2+CM[z,1]**2+CM[z,2]**2))
			median=np.median(distance)
			if T==1:
				Disk_std.append([]);Disk_std[z]=np.std(distance)
			else:
				Sph_std.append([]);Sph_std[z]=np.std(distance)

			plt.plot(longit[z],np.log10(median),'o',c=color[t])
	plt.plot([],[],'o',color='blue',label='Disk');plt.plot([],[],'o',color='red',label='Spheroid');plt.legend()
	ax.set_title( 'Distance between components and CM '+name ,fontsize=25)
	ax.set_ylabel('Logarithm of the Median of the distance',fontsize=17);ax.set_xlabel('Redshift',fontsize=25)
	plt.grid()
	plt.xticks(longit,np.round(redshift,3))
	plt.xticks(rotation=90)
	plt.savefig('CentralGalaxy/Plots/DistanceDistribution/Median_'+name+'.pdf', bbox_inches = 'tight')
	plt.close()

	R=plt.figure(figsize=(13.0, 10.0))
	ax=R.add_subplot(111)
	plt.plot(longit,np.log10(np.array(Disk_std)),'o',c='blue')
	plt.plot(longit,np.log10(np.array(Sph_std)),'o',c='red')
	plt.plot([],[],'o',color='blue',label='Disk');plt.plot([],[],'o',color='red',label='Spheroid');plt.legend()

	ax.set_title( 'Standard deviation of the distance between particles and CM of the '+name +' distribution',fontsize=20)
	ax.set_ylabel('Logarithm Standard deviation of the distances',fontsize=17);ax.set_xlabel('Redshift',fontsize=20)
	plt.grid()
	plt.xticks(longit,np.round(redshift,3))
	plt.xticks(rotation=90)
	plt.savefig('CentralGalaxy/Plots/DistanceDistribution/Std_'+name+'.png')
	plt.close()



def DelocalizedParticles(Snaps_DataDF,CM):
	cols=['rx','ry','rz']
	#	Positive situation. Particle with true negative position 

	Snaps_DataDF.loc[ ((Snaps_DataDF['rx']-CM[0])>0.5), cols[0]]=Snaps_DataDF-1
	Snaps_DataDF.loc[ ((Snaps_DataDF['ry']-CM[1])>0.5), cols[1]]=Snaps_DataDF-1
	Snaps_DataDF.loc[ ((Snaps_DataDF['rz']-CM[2])>0.5), cols[2]]=Snaps_DataDF-1
	# 	Negative situation. Particle with true positive position
	Snaps_DataDF.loc[ (Snaps_DataDF['rx']-CM[0])<-0.5, cols[0]]=Snaps_DataDF+1
	Snaps_DataDF.loc[ (Snaps_DataDF['ry']-CM[1])<-0.5, cols[1]]=Snaps_DataDF+1
	Snaps_DataDF.loc[ (Snaps_DataDF['rz']-CM[2])<-0.5, cols[2]]=Snaps_DataDF+1
	return(Snaps_DataDF)

def plotMC(CM,CM2,snaps,redshift,name,label1,label2):
	figCM= plt.figure(figsize=(13.0, 10.0))
	ax=figCM.add_subplot(111,projection='3d')
	ax.scatter(CM[:,0],CM[:,1],CM[:,2],color='blue',label=label1)
	ax.scatter(CM2[:,0],CM2[:,1],CM2[:,2],color='purple',label=label2)
	plt.legend(fontsize=12)
	ax.set_xlabel('X')
	ax.set_title('The change of the mass center',fontsize=20)
	ax.set_ylabel('Y')
	ax.set_zlabel('Z')
	ax.view_init(elev=30, azim=70);	plt.savefig('CentralGalaxy/Plots/MassCenter/'+name+'_MassCenter.png')
	ax.view_init(elev=15,azim=70);	plt.savefig('CentralGalaxy/Plots/MassCenter/'+name+'_R0_MassCenter.png')
	ax.view_init(elev=30,azim=190);	plt.savefig('CentralGalaxy/Plots/MassCenter/'+name+'_R1_MassCenter.png')
	ax.view_init(elev=15,azim=250);	plt.savefig('CentralGalaxy/Plots/MassCenter/'+name+'_R2_MassCenter.png')


	plt.close()

def plotCentralMass(Particles1,color1,label1,redshift,CM,snap,Dir,Mod=1,Particles2='None',color2='none',label2='None',zoom='yes',alpha=0.5):
	figCM= plt.figure(figsize=(13.0, 10.0))
	ax=figCM.add_subplot(111,projection='3d')
	if Mod==1:
		ax.scatter(Particles1['rx']-CM[0],Particles1['ry']-CM[1],Particles1['rz']-CM[2],c=color1,s=6, alpha=alpha,marker='o')
		ax.scatter([],[],[],c=color1,marker='o',label=label1)
	if Mod==2:
		ax.scatter(Particles1['rx']-CM[0],Particles1['ry']-CM[1],Particles1['rz']-CM[2],c=color1,s=6, alpha=alpha,marker='o')
		ax.scatter(Particles2['rx']-CM[0],Particles2['ry']-CM[1],Particles2['rz']-CM[2],c=color2,s=6, alpha=alpha,marker='o')
		ax.scatter([],[],[],c=color1,marker='o',label=label1)
		ax.scatter([],[],[],c=color2,marker='o',label=label2)
	plt.legend(fontsize=15)
	if zoom=='yes':
		ax.set_xlim(-0.004,0.004); ax.set_ylim(-0.004,0.004); ax.set_zlim(-0.004,0.004);
	ax.set_xlabel('X')
	ax.set_title('Redshift: '+str(round(redshift,3)),fontsize=20)
	ax.set_ylabel('Y')
	ax.set_zlabel('Z')

	ax.view_init(elev=30, azim=70);	plt.savefig('CentralGalaxy/Plots/'+Dir+'/Front_'+str(snap)+'.png', bbox_inches = 'tight')
	ax.view_init(elev=30,azim=250);	plt.savefig('CentralGalaxy/Plots/'+Dir+'/Back_'+str(snap)+'.png', bbox_inches = 'tight')
	
	plt.close()


def plotType(particles,CM,redshift,snap,Dir,Types):

	figCM= plt.figure(figsize=(13.0, 10.0))
	ax=figCM.add_subplot(111,projection='3d')
	color=['blue','lime','darkgreen','red']
	tips=['Gas','Thin Disk','Thick Disk','Spheroid']
	for tipo, c in zip(Types,range(len(color))):
		if tipo=='Gas' or 'Spheroid':
			alpha=0.01
		else:
			alpha=0.3
		Buffer=particles[particles['Component']==tipo]
		ax.scatter(Buffer['rx']-CM[0],Buffer['ry']-CM[1],Buffer['rz']-CM[2],c=color[c],s=6, alpha=alpha,marker='o')
		ax.scatter([],[],[],c=color[c],marker='o',label=tips[c])

	
	plt.legend(loc='lower right',fontsize=20)
	
	ax.set_xlabel('X')
	ax.set_title('Redshift: '+str(round(redshift,3)),fontsize=25)
	ax.set_ylabel('Y')
	ax.set_zlabel('Z')
	ax.set_xlim(-0.005,0.005); ax.set_ylim(-0.005,0.005); ax.set_zlim(-0.005,0.005);
	ax.view_init(elev=30, azim=70);	plt.savefig('CentralGalaxy/Plots/'+Dir+'/Front_'+str(snap)+'.png', bbox_inches = 'tight')
	ax.view_init(elev=30,azim=250);	plt.savefig('CentralGalaxy/Plots/'+Dir+'/Back_'+str(snap)+'.png', bbox_inches = 'tight')
	
	plt.close()



def plotGasTemperature(particles,CM,redshift,snap,Dir,DataHead):
	if str(snap)!='d5004.68502':
		particles=convert(particles,DataHead[snap])
	cm1 = mcol.LinearSegmentedColormap.from_list("log(T) [log10(K)]",["b","r"])
	if redshift>1:
		indexNames = particles[particles['Temperature'] > 10e3 ].index
		cnorm = mcol.Normalize(vmax=np.log10(10e3),vmin=np.log10(9e3))

	if redshift<=1:
		indexNames = particles[particles['Temperature'] > 10e3 ].index
		cnorm = mcol.Normalize(vmax=np.log10(10e3),vmin=np.log10(9e3))
	particles.drop(indexNames , inplace=True)

	cpick = cm.ScalarMappable(norm=cnorm,cmap=cm1)
	
	cpick.set_array([])

	figCM= plt.figure(figsize=(13.0, 10.0))
	ax=figCM.add_subplot(111,projection='3d')

	ax.scatter(particles['rx']-CM[0],particles['ry']-CM[1],particles['rz']-CM[2],c=cpick.to_rgba(np.log10(particles['Temperature'])),s=6, alpha=0.2,marker='o')

	ax.set_xlabel('X')
	ax.set_title('Redshift: '+str(round(redshift,3)))
	ax.set_ylabel('Y')
	ax.set_zlabel('Z')
	plt.colorbar(cpick,label="log10(T[k])");
	ax.view_init(elev=30, azim=70);	plt.savefig('CentralGalaxy/Plots/'+Dir+'/Front_'+str(snap)+'.png', bbox_inches = 'tight')
	ax.set_xlim(-0.01/3,0.01/3); ax.set_ylim(-0.01/3,0.01/3); ax.set_zlim(-0.01/3,+0.01/3);
	ax.view_init(elev=30,azim=70);	plt.savefig('CentralGalaxy/Plots/'+Dir+'/Back_'+str(snap)+'.png', bbox_inches = 'tight')
	plt.close()


def HistParticle(Data,snaps,redshift,name):
	R=plt.figure(figsize=(13.0, 10.0))
	ax=R.add_subplot(111)
	longit=np.round(np.linspace(0,len(snaps)-1,len(snaps)))
	bufhist=[];buf2hist=[]
	for s,snap in zip(range(len(snaps)),snaps):
		Buf=Data[snap][Data[snap]['itype']==-1]
		Buf2=Data[snap][Data[snap]['itype']==1]
		lenBuf=len(np.array(Buf['m']));lenBuf2=len(np.array(Buf2['m']))
		bufhist.append([lenBuf]);buf2hist.append([lenBuf2])
		ax.bar(longit[s]-0.3,lenBuf,color='dimgrey')
		ax.bar(longit[s]+0.3,lenBuf2,color='dodgerblue')
	ax.bar(longit[s],0,color='dimgrey',label='Stars')
	ax.bar(longit[s],0,color='dodgerblue',label='Gas')
	plt.legend(fontsize=20)
	plt.xticks(longit,np.round(redshift,3))
	plt.xticks(rotation=90)
	rects=ax.patches
	"""
	bufhist=np.array(bufhist); buf2hist=np.array(buf2hist)
	both=np.append(bufhist,buf2hist)
	labels=[ i for i in both]
	for rect,label in zip(rects,labels):
		height=rect.get_height()
		ax.text(rect.get_x() + rect.get_width() / 2, height + 10, label,ha='center', va='bottom',rotation=90)
	"""
	
	ax.set_ylabel('Number of particles',fontsize=25);ax.set_xlabel('Redshift',fontsize=25)
	ax.set_title(name+': Stellar and Gas particles',fontsize=25)
	plt.savefig('CentralGalaxy/Plots/Number_of_Particles/'+name+'.pdf', bbox_inches = 'tight')
	plt.close()

def SF(History,Present,snaps,redshift,name):
	R=plt.figure(figsize=(13.0, 10.0))
	ax=R.add_subplot(111)	
	longit=np.round(np.linspace(0,len(snaps)-1,len(snaps)))
	buf=[]
	for s,snap in zip(range(len(snaps)),snaps):
		buf.append([len(np.array(History[snap][History[snap]['itype']==-1]))/Present])
	buf=np.array(buf)
	plt.step(longit,buf)
	check=0
	for b in buf:
		if b<0.51 and b>0.49:
			c=b
			check=1
		if check==0 and b<0.51 and b>0.48:
			c=b
		if b<0.91 and b>0.89:
			d=b
	plt.plot([min(longit),longit[np.where(buf==c)[0]]],[0.5,0.5],color='red')
	plt.plot([min(longit),longit[np.where(buf==d)[0]]],[0.9,0.9],color='red')
	plt.plot([longit[np.where(buf==c)[0]],longit[np.where(buf==c)[0] ]],[0,0.5],color='red')
	plt.plot([longit[np.where(buf==d)[0]],longit[np.where(buf==d)[0] ]],[0,0.9],color='red')
	plt.text(longit[1],0.91,'90% of the final star population',fontsize=16)
	plt.text(longit[1],0.51,'50% of the final star population',fontsize=16)
	plt.text(longit[np.where(buf==c)[0]]+0.4,0.1,'Redshift {}'.format(redshift[np.where(buf==c)[0]]),fontsize=16,rotation=90)
	plt.text(longit[np.where(buf==d)[0]]+0.4,0.1,'Redshift {}'.format(redshift[np.where(buf==d)[0]]),fontsize=16,rotation=90)

	plt.grid()
	plt.xticks(longit,np.round(redshift,3))
	plt.xticks(rotation=90)
	ax.set_ylabel('Stars/Stars(z=0)',fontsize=25);ax.set_xlabel('Redshift',fontsize=25)
	ax.set_title(name+': Stellar Formation',fontsize=25)
	plt.savefig('CentralGalaxy/Plots/StarFormation/'+name+'.pdf', bbox_inches = 'tight')
	plt.close()


def theta(v, w,mode=0): 

	if mode==1:
		v=np.array(v)
		w=np.array(w)

		v=np.array([v[0][0],v[0][1],v[0][2]])
		w=np.array([w[0][0],w[1][0],w[2][0]])
		ang=np.abs(np.dot(v,w))
	else:
		ang=np.abs(np.dot(v,w))
	return(ang)

def plotTheta(Y1,Y2,label1,label2,redshift,snaps,name,title):
	R=plt.figure(figsize=(13.0, 10.0));ax=R.add_subplot(111)
	longit=np.round(np.linspace(0,len(snaps)-1,len(snaps)))
	plt.plot(longit,Y1,linestyle='--',marker='o',markersize=4,color='blue',label=label1)
	plt.plot(longit,Y2,linestyle='--',marker='o',markersize=4,color='red',label=label2)
	plt.legend(fontsize=20)
	plt.title(title,fontsize=25); ax.set_ylabel(r'cos($\theta$)',fontsize=20)
	ax.set_xlabel('Redshift',fontsize=20)

	plt.grid();plt.xticks(longit,np.round(redshift,3));plt.xticks(rotation=90)
	plt.savefig('CentralGalaxy/Plots/Orientation/'+name+'.pdf', bbox_inches = 'tight')

	plt.close()

def plotThetaONE(Y1,label1,redshift,snaps,name,title):
	R=plt.figure(figsize=(13.0, 10.0));ax=R.add_subplot(111)
	longit=np.round(np.linspace(0,len(snaps)-1,len(snaps)))
	plt.plot(longit,Y1,linestyle='--',marker='o',markersize=4,color='blue',label=label1)
	plt.legend(fontsize=20)
	plt.title(title,fontsize=25); ax.set_ylabel(r'cos($\theta$)',fontsize=20)
	ax.set_xlabel('Redshift',fontsize=20)

	plt.grid();plt.xticks(longit,np.round(redshift,3));plt.xticks(rotation=90)
	plt.savefig('CentralGalaxy/Plots/Orientation/'+name+'.pdf', bbox_inches = 'tight')

	plt.close()

def concatenateVV(Val,Vec1,Vec2,Vec3):
	buf=np.concatenate( (Val.reshape((1,3)),Vec1.reshape((1,3))),axis=1 )
	buf=np.concatenate((buf,Vec2.reshape((1,3))),axis=1  )
	buf=np.concatenate((buf,Vec3.reshape((1,3))),axis=1  )
	return buf

def saveEigenVV(V1,V2):
	return np.concatenate((V1,V2),axis=0)


