##############################
from Packages import *
from Def_ReadAndSave import *
from Def_CentralGalaxy import *
from InertiaTensor import *
from AngularMomentum import *
##############################
from vector import *
from  units import *
from equations import *
##############################
import datetime 
begin_time = datetime.datetime.now()
###############################

print('\n------Particles of the components of the central galaxy------\n')

print('\n-> Info:\n  	 -Column 1: Id. \n 	 -Column 2: Gas(1) or star(-1).'+
	'\n 	 -Column 3: Gas(0), thin disk(1), thick disk(2), spheroid(3)\n')

print('\n#########################################################################\n'+
	'######################### Load and save the data  #######################\n'+ 
	'#########################################################################\n')



Head=['Id','Tipe','Component']
Particles=np.loadtxt('CentralGalaxy/identity.5004.dat') #Central Galaxy
CW_Particles=np.loadtxt('CW/web2_thres19_ids_500_500_500_5004_3667.dat') #Cosmic web
redshift=np.loadtxt('CentralGalaxy/redshift_5004.dat'); redshift=redshift[:,2];redshift=np.flip(redshift)
"""

Temperature=np.loadtxt('CentralGalaxy/tempgas5004.68502.dat')



#-----------------------------------------------------------
#			Link the gas particle with their temperatures
Gas_Temperature=[]; count=0
for i,j in zip(Particles[:,1],range(len(Particles[:,1]))):
	if i==1: # Gas particle
		Gas_Temperature.append([]); Buf=Particles[j,0],Temperature[count]
		Gas_Temperature[count].extend(Buf)
		count+=1


#----------------------------------------------------------
#						Load the data
"""
snaps,root=ListData(); DATA=[];DATAMRV={}; DATABAR={}; DATAHead={}
Progress = ChargingBar('Loading data:', max=len(snaps))
for i in snaps:
	Load=np.load(('d5004_mock/MRV/'+i));#Load2=np.load((Dir[2]+'/'+i+'.npy'));Load3=pd.read_csv((Dir[0]+'/'+i+'.csv')) ;Load3.head()
	DATAMRV[i]=Load; #DATABAR[i]=Load2; DATAHead[i]=Load3; 
	time.sleep(random.uniform(0, 0.2))
	Progress.next()
Progress.finish()



mod=0;SAVE=0
while mod!="yes" and mod!="no":
	mod=str(input('-> If it is the first time running this program or perhaps some data has been lost (Ex: the data of the selected particles), enter <yes> to reset Particles_CentralGalaxy and CW/Data folders [yes/no]: '))
if mod=='yes':
	CreateDIR("Particles_CentralGalaxy");CreateDIR("./CW/Data")
print('Answer: {} .Ok'.format(mod))


#---------------------------------------------------------
#					Select the data and save

CW_ListParticles=CW_Particles.astype(int)
all_listpartCG=pd.DataFrame(Particles,columns=['ID','type','Component'])
New_all_listpartCG = all_listpartCG
ListParticles_New=np.array(all_listpartCG['ID']).astype(int)
"""
lastsnap=snaps[len(snaps)-1]

print('\nThe number of Central Galaxy\'s particles is: {}'.format(len(all_listpartCG)))
Gas_CG=Selection(DATAMRV,np.array(Gas_Temperature)[:,0].astype(int),'None',lastsnap,HeadMRV)
Gas_CG.insert(9,'Temperature',np.array(Gas_Temperature)[:,1],True)

indexNames = Gas_CG[Gas_CG['Temperature']<= 10e3 ].index #10E3=10000
Gas_CG.drop(indexNames , inplace=True)
Delete_Gas=list(np.array(Gas_CG['ID']))

New_all_listpartCG=all_listpartCG.loc[~all_listpartCG['ID'].isin(Delete_Gas)] #Mantiene las que no están en Delete_Gas

print('Now, with an T upper limit of 10^4 k the number of Central Galaxy\'s particles is: {} '.format(len(ListParticles_New)))
"""
Snaps_DataDF={};CW_SnapsDataDF={}


if  mod=='yes':
	print('\n-> The next step will take some time.'); print('')
	Progress = ChargingBar('Searching particles and saving results:', max=len(snaps))
	SAVE='yes'
else: 
	print('');Progress = ChargingBar('Searching particles:', max=len(snaps))

for i in snaps:
	time.sleep(random.uniform(0, 0.2))
	Progress.next()
	CW_DATA=Selection(DATAMRV,CW_ListParticles,'CW/Data',i,HeadMRV,SAVE); DATA=Selection(DATAMRV,ListParticles_New,'Particles_CentralGalaxy',i,HeadMRV,SAVE)
	Snaps_DataDF[i]=DATA; CW_SnapsDataDF[i]=CW_DATA
Progress.finish()

PLOT=0
while PLOT!="yes" and PLOT!="no" and PLOT!="CG" and PLOT!="CG_CW" and PLOT!="CW" and PLOT!='Temperature' and PLOT!='Particles_hist' and PLOT!='StarFormation' and PLOT!='MassCenter' and PLOT!='Distance':
	PLOT=str(input('-> Do you want plot? If you already have the plots enter <no> [yes/no].'+
		'\n   If you want a particular plot enter:\n    -[CW] to plot the Cosmic Web.\n    -[CG] to plot components of the Central Galaxy.'+
		'\n    -[MassCenter] to plot Mass Center calculation and the changes of the mass center .\n    -[CG_CW] for Central galaxy + Cosmic Web.'+
		'\n    -[Temperature] for Central galaxy Temperature\n    -[Particles_hist] Types particles histogram.\n    -[StarFormation] for the star formation.'+
		'\n    -[Distance] for the particle distance-CM\n   => '))

print('Answer: {} .Ok'.format(PLOT))


cm_control  = ''

while cm_control!='yes' and cm_control!='no':
	cm_control = str(input('-> Is the calculation of the CM necessary ? [yes/no]: '))

if PLOT=='yes':
	CreateDIR("CentralGalaxy/Plots");


if cm_control =='yes':
	print('\n#########################################################################\n'+
		'########################### Calculation of the CM #######################\n'+ 
		'#########################################################################\n')
	begin_timeCM = datetime.datetime.now()
	CreateDIR("CentralGalaxy/CM_DATA");

	def powspace(start, stop, power, num):
	    start = np.power(start, 1/float(power))
	    stop = np.power(stop, 1/float(power))
	    return np.power( np.linspace(start, stop, num=num), power) 

	################################################
	r_PostCM    = powspace(0.002,10E-20,11,61)
	r_PostCM_disk    = powspace(0.001,10E-20,11,61)
	r_subPostCM = powspace(0.0001,0.00005,2,61)
	r_subPostCM_sph = powspace(0.00015,0.00001,1,61)
	r_subPostCM_disk = powspace(0.008,0.005,1,61)
	#################################################
	CMx=[];CMy=[];CMz=[]; Particles_del={}; Particles_ker={};NParticles_del=[];NParticles_ker=[]
	CMx_CW=[];CMy_CW=[];CMz_CW=[]; ParticlesCW_del={}; ParticlesCW_ker={};NParticlesCW_del=[];NParticlesCW_ker=[]
	CMx_Disk=[];CMy_Disk=[];CMz_Disk=[]; ParticlesDisk_del={}; ParticlesDisk_ker={};NParticlesDisk_del=[];NParticlesDisk_ker=[]
	CMx_Sph=[];CMy_Sph=[];CMz_Sph=[]; ParticlesSph_del={}; ParticlesSph_ker={};NParticlesSph_del=[];NParticlesSph_ker=[]

	Progress = ChargingBar('Calculating CM [CW & CG]:', max=len(snaps))
	count=0

	CMx=np.zeros(61);CMy=np.zeros(61);CMz=np.zeros(61);NParticles_ker=np.zeros(61);NParticles_del=np.zeros(61)
	CMx_CW=np.zeros(61);CMy_CW=np.zeros(61);CMz_CW=np.zeros(61);NParticlesCW_ker=np.zeros(61);NParticlesCW_del=np.zeros(61)

	snaps_reverse = snaps[::-1]
	for i, j in zip(snaps_reverse,range(len(snaps))):
		"""
		CMx.append([]);CMy.append([]);CMz.append([]);NParticles_ker.append([]);NParticles_del.append([])
		CMx_CW.append([]);CMy_CW.append([]);CMz_CW.append([]);NParticlesCW_ker.append([]);NParticlesCW_del.append([])
		"""
		time.sleep(random.uniform(0, 0.2))
		Progress.next()
		if (60-count)== 60 : 
			CMx[60-count],CMy[60-count],CMz[60-count],Particles_ker[i],Particles_del[i],NParticles_ker[60-count],NParticles_del[60-count]=MassCenter2(Snaps_DataDF,i,'galaxy',r_PostCM[60-j],r_subPostCM[60-j],CMZ='no')
			CMx_CW[60-count],CMy_CW[60-count],CMz_CW[60-count],ParticlesCW_ker[i],ParticlesCW_del[i],NParticlesCW_ker[60-count],NParticlesCW_del[60-count]=MassCenter2(CW_SnapsDataDF,i,'LSS',r_PostCM[60-j],r_subPostCM[60-j],CMZ='no')
		else:
			G_CM0=np.array([CMx[60-count+1],CMy[60-count+1],CMz[60-count+1]])
			W_CM0=np.array([CMx_CW[60-count],CMy_CW[60-count],CMz_CW[60-count]])
			CMx[60-count],CMy[60-count],CMz[60-count],Particles_ker[i],Particles_del[i],NParticles_ker[60-count],NParticles_del[60-count]=MassCenter2(Snaps_DataDF,i,'galaxy',r_PostCM[60-j],r_subPostCM[60-j], CMZ=G_CM0)
			CMx_CW[60-count],CMy_CW[60-count],CMz_CW[60-count],ParticlesCW_ker[i],ParticlesCW_del[i],NParticlesCW_ker[60-count],NParticlesCW_del[60-count]=MassCenter2(CW_SnapsDataDF,i,'LSS',r_PostCM[60-j],r_subPostCM[60-j],CMZ=W_CM0)
		count+=1
	Progress.finish();print('\n')


	InfoCM={"snap":snaps,"redshift":redshift,'CMx':CMx,'CMy':CMy,'CMz':CMz,'Particles_in':NParticles_ker,'Particles_out':NParticles_del}
	InfoCM_CW={"snap":snaps,"redshift":redshift,'CMx':CMx_CW,'CMy':CMy_CW,'CMz':CMz_CW,'Particles_in':NParticlesCW_ker,'Particles_out':NParticlesCW_del}
	InfoCM=pd.DataFrame(InfoCM);InfoCM_CW=pd.DataFrame(InfoCM_CW)


	CM_CG=np.stack((CMx,CMy,CMz),axis=1);CM_CW=np.stack((CMx_CW,CMy_CW,CMz_CW),axis=1)
	Disk_Snaps_DataDF={};Sph_Snaps_DataDF={}
	Progress = ChargingBar('Searching the delocalized part. & calculating the C.O.Ms [Components] :', max=len(snaps))

	CMx_Disk=np.zeros(61);CMy_Disk=np.zeros(61);CMz_Disk=np.zeros(61);NParticlesDisk_ker=np.zeros(61);NParticlesDisk_del=np.zeros(61)
	CMx_Sph=np.zeros(61);CMy_Sph=np.zeros(61);CMz_Sph=np.zeros(61);NParticlesSph_ker=np.zeros(61);NParticlesSph_del=np.zeros(61)

	for i, j in zip(snaps_reverse,range(len(snaps))):
		Snaps_DataDF[i]=DelocalizedParticles(Snaps_DataDF[i],CM_CG[j]); Snaps_DataDF[i].insert(10, "Component", np.array(New_all_listpartCG['Component']),True)
		Disk_Snaps_DataDF[i]=Snaps_DataDF[i].loc[ (Snaps_DataDF[i]['Component']==1) | (Snaps_DataDF[i]['Component']==2) | (Snaps_DataDF[i]['Component']==0) ]
		Sph_Snaps_DataDF[i]=Snaps_DataDF[i].loc[Snaps_DataDF[i]['Component']==3]
		Disk_Snaps_DataDF[i]=Disk_Snaps_DataDF[i].drop(columns=['radius']);	Sph_Snaps_DataDF[i]=Sph_Snaps_DataDF[i].drop(['radius'], axis=1)

		"""
		CMx_Disk.append([]);CMy_Disk.append([]);CMz_Disk.append([]);NParticlesDisk_ker.append([]);NParticlesDisk_del.append([])
		CMx_Sph.append([]);CMy_Sph.append([]);CMz_Sph.append([]);NParticlesSph_ker.append([]);NParticlesSph_del.append([])
		"""
		if (60-j)==60 : 
			CMx_Disk[60-j],CMy_Disk[60-j],CMz_Disk[60-j],ParticlesDisk_ker[i],ParticlesDisk_del[i],NParticlesDisk_ker[60-j],NParticlesDisk_del[60-j]=MassCenter2(Disk_Snaps_DataDF,i,'galaxy',r_PostCM_disk[60-j],r_subPostCM_disk[60-j],CMZ='no')
			CMx_Sph[60-j],CMy_Sph[60-j],CMz_Sph[60-j],ParticlesSph_ker[i],ParticlesSph_del[i],NParticlesSph_ker[60-j],NParticlesSph_del[60-j]=MassCenter2(Sph_Snaps_DataDF,i,'galaxy',r_PostCM[60-j],r_subPostCM_sph[60-j],CMZ='no')
		else:
			D_CM0=np.array([CMx_Disk[60-j+1],CMy_Disk[60-j+1],CMz_Disk[60-j+1]])
			S_CM0= np.array([CMx_Sph[60-j+1],CMy_Sph[60-j+1],CMz_Sph[60-j+1]])
			CMx_Disk[60-j],CMy_Disk[60-j],CMz_Disk[60-j],ParticlesDisk_ker[i],ParticlesDisk_del[i],NParticlesDisk_ker[60-j],NParticlesDisk_del[60-j]=MassCenter2(Disk_Snaps_DataDF,i,'galaxy',r_PostCM_disk[60-j],r_subPostCM_disk[60-j],CMZ=D_CM0)
			CMx_Sph[60-j],CMy_Sph[60-j],CMz_Sph[60-j],ParticlesSph_ker[i],ParticlesSph_del[i],NParticlesSph_ker[60-j],NParticlesSph_del[60-j]=MassCenter2(Sph_Snaps_DataDF,i,'galaxy',r_PostCM[60-j],r_subPostCM_sph[60-j],CMZ=S_CM0)


		CW_SnapsDataDF[i]=DelocalizedParticles(CW_SnapsDataDF[i],CM_CG[60-j])
		ParticlesCW_ker[i]=DelocalizedParticles(ParticlesCW_ker[i],CM_CW[60-j])
		ParticlesCW_del[i]=DelocalizedParticles(ParticlesCW_del[i],CM_CW[60-j])
		time.sleep(random.uniform(0, 0.2))
		Progress.next()
	Progress.finish()

	CM_Disk=np.stack((CMx_Disk,CMy_Disk,CMz_Disk),axis=1);CM_Sph=np.stack((CMx_Sph,CMy_Sph,CMz_Sph),axis=1)

	InfoCM_Disk={"snap":snaps,"redshift":redshift,'CMx':CMx_Disk,'CMy':CMy_Disk,'CMz':CMz_Disk,'Particles_in':NParticlesDisk_ker,'Particles_out':NParticlesDisk_del}
	InfoCM_Sph={"snap":snaps,"redshift":redshift,'CMx':CMx_Sph,'CMy':CMy_Sph,'CMz':CMz_Sph,'Particles_in':NParticlesSph_ker,'Particles_out':NParticlesSph_del}

	InfoCM_Disk=pd.DataFrame(InfoCM_Disk);InfoCM_Sph=pd.DataFrame(InfoCM_Sph)
	InfoCM_CW.to_csv(('CentralGalaxy/CM_DATA/CW_InfoCM.csv'),header=True, index=False)
	InfoCM.to_csv(('CentralGalaxy/CM_DATA/CG_InfoCM.csv'),header=True, index=False)

	InfoCM_Sph.to_csv(('CentralGalaxy/CM_DATA/Spheroid_InfoCM.csv'),header=True, index=False)
	InfoCM_Disk.to_csv(('CentralGalaxy/CM_DATA/Disk_InfoCM.csv'),header=True, index=False)
	print('-> CM-data saved in /CentralGalaxy/CM_DATA as CW_InfoCM');print('-> CM-data saved in /CentralGalaxy/CM_DATA as CG_InfoCM\n')
	print('-> CM-data saved in /CentralGalaxy/CM_DATA as Disk_InfoCM');print('-> CM-data saved in /CentralGalaxy/CM_DATA as Spheroid_InfoCM')	
	print('Time: {}'.format(datetime.datetime.now() - begin_timeCM))

if cm_control== 'no':
	from PostCM_V3 import radius_particle
	fileDir = r"./CentralGalaxy/CM_DATA"
	fileExt = r".csv"
	files=[a for a in os.listdir(fileDir) if a.endswith(fileExt)]
	files.sort()

	CM_CGD = pd.read_csv(fileDir+'/'+files[0])
	CM_CWD = pd.read_csv(fileDir+'/'+files[1])
	CM_DiskD = pd.read_csv(fileDir+'/'+files[2])
	CM_SphD = pd.read_csv(fileDir+'/'+files[3])

	CM_Disk = np.array(CM_DiskD[['CMx','CMy','CMz']])
	CM_Sph = np.array(CM_SphD[['CMx','CMy','CMz']])
	CM_CW = np.array(CM_CWD[['CMx','CMy','CMz']])
	CM_CG = np.array(CM_CGD[['CMx','CMy','CMz']])

	def add_data(dataframe, snap, CM,i):
		radius=radius_particle(dataframe,snap,CM[i,:]);
		dataframe[snap].insert(8,"radius",radius,True)
		return(dataframe[snap])
	Disk_Snaps_DataDF={};Sph_Snaps_DataDF={}
	for (snap,i) in zip(snaps,range(len(snaps))):
		CW_SnapsDataDF[snap] = add_data(CW_SnapsDataDF,snap,CM_CW,i)
		Snaps_DataDF[snap] = add_data(Snaps_DataDF,snap,CM_CG,i)

		CW_SnapsDataDF[snap]=DelocalizedParticles(CW_SnapsDataDF[snap],CM_CW[i,:]);
		Snaps_DataDF[snap]=DelocalizedParticles(Snaps_DataDF[snap],CM_CG[i,:]); Snaps_DataDF[snap].insert(9, "Component", np.array(New_all_listpartCG['Component']),True)
		Disk_Snaps_DataDF[snap]=Snaps_DataDF[snap].loc[ (Snaps_DataDF[snap]['Component']==1) | (Snaps_DataDF[snap]['Component']==2) | (Snaps_DataDF[snap]['Component']==0) ]
		Sph_Snaps_DataDF[snap]=Snaps_DataDF[snap].loc[Snaps_DataDF[snap]['Component']==3]

		Disk_Snaps_DataDF[snap]=Disk_Snaps_DataDF[snap].drop(columns=['radius']);	Sph_Snaps_DataDF[snap]=Sph_Snaps_DataDF[snap].drop(['radius'], axis=1)
		Disk_Snaps_DataDF[snap] = add_data(Disk_Snaps_DataDF,snap,CM_Disk,i)
		Sph_Snaps_DataDF[snap] = add_data(Sph_Snaps_DataDF,snap,CM_Sph,i)





print('\n#########################################################################\n'+
	'########################### Structure Information #######################\n'+ 
	'###############################-Redshift=0-##############################')
print('')

row0=['Name','Nº of Particles', 'Total Mass [10^{10} Msun]', 'Gas Mass[10^{10} Msun]','Stellar Mass [10^{10} Msun]']
i=snaps[len(snaps)-1]
GasMass_CW=CW_SnapsDataDF[i][CW_SnapsDataDF[i]['itype']==1]['m'].sum()*convMass; 
GasMass_CG=Snaps_DataDF[i][Snaps_DataDF[i]['itype']==1]['m'].sum()*convMass
StellarMass_CW=CW_SnapsDataDF[i][CW_SnapsDataDF[i]['itype']==-1]['m'].sum()*convMass; 
StellarMass_CG=Snaps_DataDF[i][Snaps_DataDF[i]['itype']==-1]['m'].sum()*convMass; 

Disk_CGinformation=Snaps_DataDF[i].loc[(Snaps_DataDF[i]['Component']==1) | (Snaps_DataDF[i]['Component']==2) | (Snaps_DataDF[i]['Component']==0) ]
Spheroid_CGinformation=Snaps_DataDF[i][Snaps_DataDF[i]['Component']==3]


DiskStars=Disk_CGinformation[Disk_CGinformation['itype']==-1]['m'].sum()*convMass; 
DiskGas=Disk_CGinformation[Disk_CGinformation['itype']==1]['m'].sum()*convMass 
SphStars=Spheroid_CGinformation[Spheroid_CGinformation['itype']==-1]['m'].sum()*convMass; 
SphGas=Spheroid_CGinformation[Spheroid_CGinformation['itype']==1]['m'].sum()*convMass; 

rows=[['CW', len(np.array(CW_SnapsDataDF[i]['m'])),round(CW_SnapsDataDF[i]['m'].sum()*convMass/1e10,2), round(GasMass_CW/1e10,2) ,round(StellarMass_CW/1e10,2)],
['Central Galaxy',len(np.array(Snaps_DataDF[i]['m'])),round(Snaps_DataDF[i]['m'].sum()*convMass/1e10,2),round(GasMass_CG/1e10,2),round(StellarMass_CG/1e10,2) ],
['Central Galaxy Disk',len(np.array(Disk_CGinformation['m'])),round(Disk_CGinformation['m'].sum()*convMass/1e10,2),round(DiskGas/1e10,2),round(DiskStars/1e10,2)],
['Central Galaxy Spheroid',len(np.array(Spheroid_CGinformation['m'])),round(Spheroid_CGinformation['m'].sum()*convMass/1e10,2),round(SphGas,2),round(SphStars/1e10,2)  ]]
Table(row0,rows)




if PLOT!='no':
	print('\n#########################################################################\n'+
		'################################# Plotting ##############################\n'+ 
		'#########################################################################\n')

	if PLOT=='MassCenter' or PLOT=='yes':
		CreateDIR("CentralGalaxy/Plots/MassCenter")
		plotMC(CM_CW,CM_CG,snaps,redshift,'CWCG','Cosmic Web','Central Galaxy')	
		plotMC(CM_Disk,CM_Sph,snaps,redshift,'DiskSph','Disk','Spheroid')	
		plotMC(CM_CW,CM_Sph,snaps,redshift,'DiskCW','Cosmic Web','Spheroid')	

		print('The changes of the mass center has been plotted\n')
		
	
	if (PLOT=='MassCenter' or PLOT=='yes' ) and cm_control=='yes':
		CreateDIR("CentralGalaxy/Plots/CM_CG"); CreateDIR("CentralGalaxy/Plots/CM_CW"); 
		
		Progress = ChargingBar('Ploting: Central Mass Calculation', max=len(snaps))
		for i,j in zip(snaps,range(len(snaps))):
			time.sleep(random.uniform(0, 0.2))
			Progress.next()
			plotCentralMass(ParticlesCW_ker[i],'green','Included',redshift[j],CM_CW[j],i,'CM_CW',2,ParticlesCW_del[i],'red','Depreciated',alpha=0.3)
			plotCentralMass(Particles_ker[i],'green','Included',redshift[j],CM_CG[j],i,'CM_CG',2,Particles_del[i],'red','Depreciated')
		Progress.finish()
		print('')

	if PLOT=='CW' or PLOT=='yes':
		CreateDIR("CentralGalaxy/Plots/CW"); 
		Progress = ChargingBar('Ploting: CW ', max=len(snaps))
		for i,j in zip(snaps,range(len(snaps))):
			time.sleep(random.uniform(0, 0.2))
			Progress.next()
			plotCentralMass(CW_SnapsDataDF[i],'blue','Cosmic Web',redshift[j],CM_CG[j],i,'CW',1,alpha=0.3,zoom='no')
		Progress.finish()
		print('')

	if PLOT=='CG_CW'or PLOT=='yes':	
		CreateDIR("CentralGalaxy/Plots/CG_CW")
		Progress = ChargingBar('Ploting: Central galaxy and CW ', max=len(snaps))
		for i,j in zip(snaps,range(len(snaps))):
			time.sleep(random.uniform(0, 0.2))
			Progress.next()
			plotCentralMass(Snaps_DataDF[i],'green','Central Galaxy',redshift[j],CM_CG[j],i,'CG_CW',2,CW_SnapsDataDF[i],'blue','Cosmic Web','yes',alpha=0.01)
		Progress.finish()
		print('')

	if PLOT=='CG' or PLOT=='yes':	
		CreateDIR('CentralGalaxy/Plots/CG')
		Progress = ChargingBar('Ploting: Central galaxy components ', max=len(snaps))
		Types=[0,1,2,3]
		for i,j in zip(snaps,range(len(snaps))):
			time.sleep(random.uniform(0, 0.2))
			Progress.next()
			plotType(Snaps_DataDF[i],CM_CG[j],redshift[j],i,'CG',Types)
		Progress.finish()
		print('')
	"""
	if PLOT=='Temperature' or PLOT=='yes':	
		CreateDIR("CentralGalaxy/Plots/Temperature")
		CG_Temperature={}

		lastsnap=snaps[(len(snaps)-1)]
		Progress = ChargingBar('Ploting: Central galaxy Temperature ', max=len(snaps))
		for i,j in zip(snaps,range(len(snaps))):
			time.sleep(random.uniform(0, 0.2))
			Progress.next()
			CG_Temperature[i]=Selection(DATAMRV,np.array(Gas_Temperature)[:,0].astype(int),'None',i,HeadMRV)

			T_baryon=Selection(DATABAR,np.array(Gas_Temperature)[:,0].astype(int),'None',i,HeadBAR)
			if i!=lastsnap:
				CG_Temperature[i].insert(9,'Temperature',T_baryon['e'],True)
			if str(i)==str(lastsnap):
				CG_Temperature[i].insert(9,'Temperature',np.array(Gas_Temperature)[:,1],True)
			plotGasTemperature(CG_Temperature[i],CM_CG[j],redshift[j],i,'Temperature',DATAHead)		
		
		Progress.finish()
		print('')
	"""
	if PLOT=='Particles_hist' or PLOT=='yes':
		CreateDIR('CentralGalaxy/Plots/Number_of_Particles')

		HistParticle(Snaps_DataDF,snaps,redshift,'CG')
		HistParticle(CW_SnapsDataDF,snaps,redshift,'CW')
		Disk_CGinformation={}; Spheroid_CGinformation={}
		for i in snaps:
			Disk_CGinformation[i]=Snaps_DataDF[i].loc[(Snaps_DataDF[i]['Component']==1) | (Snaps_DataDF[i]['Component']==2) ]
			Spheroid_CGinformation[i]=Snaps_DataDF[i][Snaps_DataDF[i]['Component']==3]
		HistParticle(Disk_CGinformation,snaps,redshift,'Disk')
		HistParticle(Spheroid_CGinformation,snaps,redshift,'Spheroid')
		print('The histogram of the types of particles has been plotted \n')

	if PLOT=='StarFormation' or PLOT=='yes':
		CreateDIR('CentralGalaxy/Plots/StarFormation')
		Disk_CGinformation={}; Spheroid_CGinformation={}
		for i in snaps:
			Disk_CGinformation[i]=Snaps_DataDF[i].loc[(Snaps_DataDF[i]['Component']==1) | (Snaps_DataDF[i]['Component']==2) ]
			Spheroid_CGinformation[i]=Snaps_DataDF[i][Snaps_DataDF[i]['Component']==3]
		lastsnap=snaps[len(snaps)-1]
		NumberDisk=len(np.array(Disk_CGinformation[lastsnap]['m']))
		NumberSph=len(np.array(Spheroid_CGinformation[lastsnap]['m']))
		SF(Disk_CGinformation,NumberDisk,snaps,redshift,'Disk')
		SF(Spheroid_CGinformation,NumberSph,snaps,redshift,'Spheroid')
		print('The star formation has been plotted \n')

	if PLOT=='Distance' or PLOT=='yes':
		#To see the distance between the CGs components and CGs CM
		CreateDIR('CentralGalaxy/Plots/DistanceDistribution')
		CMdistance(Snaps_DataDF,CM_CG,snaps,redshift,[1,3],'Centragl_Galaxy')
		CMdistance(Snaps_DataDF,CM_CW,snaps,redshift,[1,3],'Cosmic_Web')
		print('The distance between components and CM has been plotted \n')





print('\n#########################################################################\n'+
	'########################### Inertia Tensor ##############################\n'+ 
	'#########################################################################\n')

# Data of the particles : Snaps_DataDF, Disk_Snaps_DataDF, Sph_Snaps_DataDF, CW_SnapsDataDF
# Data of the CM: CM_CG,CM_CW,CM_Disk,CM_Sph
opcion_tensorinercia=0
while str(opcion_tensorinercia)!=str(1) and str(opcion_tensorinercia)!=str(2) and str(opcion_tensorinercia)!=str(3) and str(opcion_tensorinercia)!=str(4):
	opcion_tensorinercia=input('What is the reference sistem of the inertia tensor of CW,CG,Sph and Disk\n'+
		'	1 -> CW,CG,CG,CG\n 	2 -> CW,CW,CW,CW\n 	3-> CW, CG, CSph, CDisk\n 	4-> CG,CG,CG,CG \n...')
print('Answer: {} .Ok'.format(opcion_tensorinercia))

if int(opcion_tensorinercia)==1:
	abc_cms0={'a':CM_CW,'b':CM_CG,'c':CM_CG,'d':CM_CG}
if int(opcion_tensorinercia)==2:
	abc_cms0={'a':CM_CW,'b':CM_CW,'c':CM_CW,'d':CM_CW}
if int(opcion_tensorinercia)==3:
	abc_cms0={'a':CM_CW,'b':CM_CG,'c':CM_Sph,'d':CM_Disk}
if int(opcion_tensorinercia)==4:
	abc_cms0={'a':CM_CG,'b':CM_CG,'c':CM_CG,'d':CM_CG}

Progress = ChargingBar('Calculating the Inertia Tensor and minor axis:', max=len(snaps))
I_CG={};eigenvalues_CG={}; eigenvectors_CG={}; axis_CG={}; save_EVCG=[]
I_CW={};eigenvalues_CW={}; eigenvectors_CW={}; axis_CW={}; save_EVCW=[]
I_Sph={};eigenvalues_Sph={}; eigenvectors_Sph={} ; axis_Sph={}; save_EVCSph=[]
I_Disk={};eigenvalues_Disk={}; eigenvectors_Disk={}; axis_Disk={}; save_EVCDisk=[]

radius_control = ''

while radius_control!='yes' and radius_control!='no':
	radius_control = str(input('-> Reduce the galaxy to a radius = 0.003 ? [yes/no]: '))

print('Answer :',radius_control)
eigenfix=''
while eigenfix!='no' and eigenfix!='yes':
	eigenfix = str(input('Correct the eigenvectors ? [yes/no] : '))
print('Answer :',eigenfix)
for i,j in zip(snaps,range(len(snaps))):
	time.sleep(random.uniform(0, 0.2))
	Progress.next()
	i=snaps[60-j]; fix_i=snaps[60]
	j=60-j;

	if j==60:
		initial='yes'	
		buf_eigenvector1=[];buf_eigenvector2=[];buf_eigenvector3=[];buf_eigenvector4=[]
		pbuf_eigenvector1=[];pbuf_eigenvector2=[];pbuf_eigenvector3=[];pbuf_eigenvector4=[]

	else: 
		initial='no'

	I_CG[i],eigenvalues_CG[i],eigenvectors_CG[i]=InertiaTensor(Snaps_DataDF[i],abc_cms0['b'],j,buf_eigenvector1,pbuf_eigenvector1,initial,3,fixeigenval=eigenfix); 
	axis_CG[i]=MinorAxis(eigenvalues_CG[i],Snaps_DataDF[i]);
	buf_eigenvector1=eigenvectors_CG[fix_i];pbuf_eigenvector1=eigenvectors_CG[i]; #z0 z anteior

	I_CW[i],eigenvalues_CW[i],eigenvectors_CW[i]=InertiaTensor(CW_SnapsDataDF[i],abc_cms0['a'],j,buf_eigenvector2,pbuf_eigenvector2,initial,1,'cw');
	axis_CW[i]=MinorAxis(eigenvalues_CW[i],CW_SnapsDataDF[i])
	buf_eigenvector2=eigenvectors_CW[fix_i];pbuf_eigenvector2=eigenvectors_CW[i];
	if radius_control =='yes':
		radio = 0.003
		Disk_Snaps_DataDF[i]=Disk_Snaps_DataDF[i][Disk_Snaps_DataDF[i]['radius']<=radio]

	I_Disk[i],eigenvalues_Disk[i],eigenvectors_Disk[i]=InertiaTensor(Disk_Snaps_DataDF[i],abc_cms0['d'],j,buf_eigenvector3,pbuf_eigenvector3,initial,3,fixeigenval=eigenfix);
	axis_Disk[i]=MinorAxis(eigenvalues_Disk[i],Disk_Snaps_DataDF[i]);
	buf_eigenvector3=eigenvectors_Disk[fix_i];pbuf_eigenvector3=eigenvectors_Disk[i]; 

	I_Sph[i],eigenvalues_Sph[i],eigenvectors_Sph[i]=InertiaTensor(Sph_Snaps_DataDF[i],abc_cms0['c'],j,buf_eigenvector4,pbuf_eigenvector4,initial,3,'sph'); 
	axis_Sph[i]=MinorAxis(eigenvalues_Sph[i],Sph_Snaps_DataDF[i])
	buf_eigenvector4=eigenvectors_Sph[fix_i];pbuf_eigenvector4=eigenvectors_Sph[i]; 
	

	if j==60:
		save_EVCDisk=concatenateVV(eigenvalues_Disk[i],eigenvectors_Disk[i][:,0],eigenvectors_Disk[i][:,1],eigenvectors_Disk[i][:,2])
		save_EVCG=concatenateVV(eigenvalues_CG[i],eigenvectors_CG[i][:,0],eigenvectors_CG[i][:,1],eigenvectors_CG[i][:,2])
		save_EVCW=concatenateVV(eigenvalues_CW[i],eigenvectors_CW[i][:,0],eigenvectors_CW[i][:,1],eigenvectors_CW[i][:,2])
		save_EVCSph=concatenateVV(eigenvalues_Sph[i],eigenvectors_Sph[i][:,0],eigenvectors_Sph[i][:,1],eigenvectors_Sph[i][:,2])

	else:
		buf1=concatenateVV(eigenvalues_Disk[i],eigenvectors_Disk[i][:,0],eigenvectors_Disk[i][:,1],eigenvectors_Disk[i][:,2])
		buf2=concatenateVV(eigenvalues_CG[i],eigenvectors_CG[i][:,0],eigenvectors_CG[i][:,1],eigenvectors_CG[i][:,2])
		buf3=concatenateVV(eigenvalues_CW[i],eigenvectors_CW[i][:,0],eigenvectors_CW[i][:,1],eigenvectors_CW[i][:,2])
		buf4=concatenateVV(eigenvalues_Sph[i],eigenvectors_Sph[i][:,0],eigenvectors_Sph[i][:,1],eigenvectors_Sph[i][:,2])

		save_EVCDisk=saveEigenVV(save_EVCDisk,buf1)
		save_EVCG=saveEigenVV(save_EVCG,buf2)
		save_EVCW=saveEigenVV(save_EVCW,buf3)
		save_EVCSph=saveEigenVV(save_EVCSph,buf4)
Progress.finish()

# saving the eigenvalues
save_columns=['eVal_Minor','eVal_Medium',
	'eVal_Maximum','eVec1_Minor','eVec2_Minor','eVec3_Minor','eVec1_Medium',
	'eVec2_Medium','eVec3_Medium','eVec1_Maximum','eVec2_Maximum','eVec3_Maximum']

save_EVCDisk = pd.DataFrame(save_EVCDisk,columns=save_columns)
save_EVCDisk.insert(0, "Redshift", np.flip(redshift), True) ; save_EVCDisk.insert(0, "Snap", np.flip(snaps), True) 

save_EVCSph = pd.DataFrame(save_EVCSph,columns=save_columns)
save_EVCSph.insert(0, "Redshift", np.flip(redshift), True) ; save_EVCSph.insert(0, "Snap", np.flip(snaps), True) 

save_EVCG = pd.DataFrame(save_EVCG,columns=save_columns)
save_EVCG.insert(0, "Redshift", np.flip(redshift), True) ; save_EVCG.insert(0, "Snap", np.flip(snaps), True)

save_EVCW = pd.DataFrame(save_EVCW,columns=save_columns)
save_EVCW.insert(0, "Redshift", np.flip(redshift), True) ; save_EVCW.insert(0, "Snap", np.flip(snaps), True)  

CreateDIR('CentralGalaxy/Values_eigenvalues')

save_EVCDisk.to_csv('CentralGalaxy/Values_eigenvalues/Disk.txt', sep=" ")
save_EVCSph.to_csv('CentralGalaxy/Values_eigenvalues/Spheroid.txt', sep=" ")
save_EVCW.to_csv('CentralGalaxy/Values_eigenvalues/CW.txt', sep=" ")
save_EVCG.to_csv('CentralGalaxy/Values_eigenvalues/CG.txt', sep=" ")
########################

Triaxility_CG=[];Triaxility_CW=[];Triaxility_Disk=[];Triaxility_Sph=[] 
Ellipticity_CG=[];Ellipticity_CW=[];Ellipticity_Disk=[];Ellipticity_Sph=[]
Prolateness_CG=[];Prolateness_CW=[];Prolateness_Disk=[];Prolateness_Sph=[]
Progress = ChargingBar('Calculating the deformation parameters:', max=len(snaps))
for i,j in zip(snaps,range(len(snaps))):
	time.sleep(random.uniform(0, 0.2))
	Progress.next()

	Triaxility_CG.append([]);Triaxility_CW.append([]);Triaxility_Disk.append([]);Triaxility_Sph.append([])
	Ellipticity_CG.append([]);Ellipticity_CW.append([]);Ellipticity_Disk.append([]);Ellipticity_Sph.append([])
	Prolateness_CG.append([]);Prolateness_CW.append([]);Prolateness_Disk.append([]);Prolateness_Sph.append([])

	Triaxility_CG[j],Ellipticity_CG[j],Prolateness_CG[j]=Deformation(axis_CG[i][0],axis_CG[i][1],axis_CG[i][2])
	Triaxility_CW[j],Ellipticity_CW[j],Prolateness_CW[j]=Deformation(axis_CW[i][0],axis_CW[i][1],axis_CW[i][2])
	Triaxility_Disk[j],Ellipticity_Disk[j],Prolateness_Disk[j]=Deformation(axis_Disk[i][0],axis_Disk[i][1],axis_Disk[i][2])
	Triaxility_Sph[j],Ellipticity_Sph[j],Prolateness_Sph[j]=Deformation(axis_Sph[i][0],axis_Sph[i][1],axis_Sph[i][2])

Progress.finish()


CreateDIR('CentralGalaxy/Plots/InertiaTensor')
colors = cm.rainbow(np.linspace(0, 1, 61))
plt.figure(figsize=(13.0, 10.0))

AitoffProjection(eigenvectors_CW,snaps,221,'Cosmic Web',1)
AitoffProjection(eigenvectors_CG,snaps,222, 'Central Galaxy',3)
AitoffProjection(eigenvectors_Disk,snaps,223, 'Disk',3)
AitoffProjection(eigenvectors_Sph,snaps,224, 'Spheroid',3)

plt.savefig('CentralGalaxy/Plots/InertiaTensor/InertiaTensor.pdf', bbox_inches = 'tight')
plt.close()

CreateDIR('CentralGalaxy/Plots/Axis')
axis_CG=np.array(list(axis_CG.values())); axis_CW=np.array(list(axis_CW.values()));Triaxility_CG=np.array(Triaxility_CG);Triaxility_CW=np.array(Triaxility_CW)
axis_Disk=np.array(list(axis_Disk.values())) ;  axis_Sph=np.array(list(axis_Sph.values())); Triaxility_Disk=np.array(Triaxility_Disk);Triaxility_Sph=np.array(Triaxility_Sph)
#these arrays have been made from z=0 to z=10, so they need np.flip 
axis_CG=np.flip(axis_CG); axis_CW=np.flip(axis_CW);  
axis_Disk=np.flip(axis_Disk); axis_Sph=np.flip(axis_Sph);
# Now the order is the correct one but the axis have been change to a,b,c -> c,b,a 

PlotMinorAxis('Cosmic_Web_Central_Galaxy','All',axis_CG,'a -Central Galaxy','magenta','darkmagenta','purple',axis_CW,'a- Cosmic Web','blue','royalblue','navy',redshift)
PlotMinorAxis('Disk_Spheroid','All',axis_Sph,'a -Spheroid','red','darkred','firebrick',axis_Disk,'a- Disk','green','lime','darkgreen',redshift)
PlotOneAxis('a',axis_CW[:,2],'Cosmic Web','blue',axis_CG[:,2],'Central Galaxy','magenta',axis_Disk[:,2],'Disk','green',axis_Sph[:,2],'Spheroid','red',redshift)
PlotOneAxis('b',axis_CW[:,1],'Cosmic Web','blue',axis_CG[:,1],'Central Galaxy','magenta',axis_Disk[:,1],'Disk','green',axis_Sph[:,1],'Spheroid','red',redshift)
PlotOneAxis('c',axis_CW[:,0],'Cosmic Web','blue',axis_CG[:,0],'Central Galaxy','magenta',axis_Disk[:,0],'Disk','green',axis_Sph[:,0],'Spheroid','red',redshift)
print('The minor axis behavior has been plotted. Check CentralGalaxy/Plots/Axis.')
PlotOneAxis('Triaxility',Triaxility_CW,'Cosmic Web','blue',Triaxility_CG,'Central Galaxy','magenta',Triaxility_Disk,'Disk','green',Triaxility_Sph,'Spheroid','red',redshift)
PlotOneAxis('Ellipticity',Ellipticity_CW,'Cosmic Web','blue',Ellipticity_CG,'Central Galaxy','magenta',Ellipticity_Disk,'Disk','green',Ellipticity_Sph,'Spheroid','red',redshift)
PlotOneAxis('Prolateness',Prolateness_CW,'Cosmic Web','blue',Prolateness_CG,'Central Galaxy','magenta',Prolateness_Disk,'Disk','green',Prolateness_Sph,'Spheroid','red',redshift)
print('The deformation parameters behavior has been plotted. Check CentralGalaxy/Plots/Axis.')


print('\n#########################################################################\n'+
	'########################### Angular Momentum ############################\n'+ 
	'#########################################################################\n')
opcion_momentoangular=0
while str(opcion_momentoangular)!=str(1) and str(opcion_momentoangular)!=str(2) and str(opcion_momentoangular)!=str(3) and str(opcion_momentoangular)!=str(4):
	opcion_momentoangular=input('What is the reference sistem of the angular momentum of CW,CG,Sph and Disk\n'+
		'	1 -> CW,CG,CG,CG\n 	2 -> CW,CW,CW,CW\n 	3-> CW, CG, CSph, CDisk\n 	4-> CG,CG,CG,CG \n...')
print('Answer: {} .Ok'.format(opcion_momentoangular))

if int(opcion_momentoangular)==1:
	abc_cms={'a':CM_CW,'b':CM_CG,'c':CM_CG,'d':CM_CG}
if int(opcion_momentoangular)==2:
	abc_cms={'a':CM_CW,'b':CM_CW,'c':CM_CW,'d':CM_CW}
if int(opcion_momentoangular)==3:
	abc_cms={'a':CM_CW,'b':CM_CG,'c':CM_Sph,'d':CM_Disk}
if int(opcion_momentoangular)==4:
	abc_cms={'a':CM_CG,'b':CM_CG,'c':CM_CG,'d':CM_CG}

Progress = ChargingBar('Calculating the Angular Momentum:', max=len(snaps))
AngularMomentum_CW={};AngularMomentum_CG={};AngularMomentum_Disk={};AngularMomentum_Sph={}; 
for i,j in zip(snaps,range(len(snaps))):
	time.sleep(random.uniform(0, 0.2))
	Progress.next()
	AngularMomentum_CW[i]=AngularMomentum(CW_SnapsDataDF[i],abc_cms['a'][j])
	AngularMomentum_CG[i]=AngularMomentum(Snaps_DataDF[i],abc_cms['b'][j])
	AngularMomentum_Sph[i]=AngularMomentum(Sph_Snaps_DataDF[i],abc_cms['c'][j])
	AngularMomentum_Disk[i]=AngularMomentum(Disk_Snaps_DataDF[i],abc_cms['d'][j])

Progress.finish()

CreateDIR('CentralGalaxy/Plots/AngularMomentum')

colors = cm.rainbow(np.linspace(0, 1, 61))
plt.figure(figsize=(13.0, 10.0))
AitoffProjection(AngularMomentum_CW,snaps,221,'Cosmic Web',1)
AitoffProjection(AngularMomentum_CG,snaps,222,'Central Galaxy',1)
AitoffProjection(AngularMomentum_Disk,snaps,223,'Disk',1)
AitoffProjection(AngularMomentum_Sph,snaps,224,'Spheroid',1)
plt.savefig('CentralGalaxy/Plots/AngularMomentum/AngularMomentum.pdf', bbox_inches = 'tight')
plt.close()
print('The Angular Momentum has been plotted. Check CentralGalaxy/Plots/AngularMomentum.')


AM_CW=np.array(list(AngularMomentum_CW.values()));AM_CG=np.array(list(AngularMomentum_CG.values()))
AM_Disk=np.array(list(AngularMomentum_Disk.values()));AM_Sph=np.array(list(AngularMomentum_Sph.values()))

R=plt.figure(figsize=(13.0, 10.0))
ax=R.add_subplot(111)
longit=np.round(np.linspace(0,len(snaps)-1,len(snaps)))
a=[];b=[];c=[];d=[]
for i in range(len(snaps)):
	a.append(magnitude(AM_CW[i,:]));b.append(magnitude(AM_CG[i,:]));c.append(magnitude(AM_Disk[i,:]));d.append(magnitude(AM_Sph[i,:]))

plt.grid()
plt.plot(longit,a,linestyle='--',marker='o',markersize=4,color='blue',label='Cosmic Web')
plt.plot(longit,b,linestyle='--',marker='o',markersize=4,color='magenta',label='Central Galaxy')
plt.plot(longit,c,linestyle='--',marker='o',markersize=4,color='green',label='Disk')
plt.plot(longit,d,linestyle='--',marker='o',markersize=4,color='red',label='Spheroid')
plt.legend(fontsize=20)
plt.title('Magnitude of the Angular Momentum',fontsize=25); ax.set_xlabel('Redshift',fontsize=25)
plt.xticks(longit,np.round(redshift,3));plt.xticks(rotation=90)
plt.savefig('CentralGalaxy/Plots/AngularMomentum/Magnitude_AngularMomentum.pdf', bbox_inches = 'tight')

plt.close()


print('\n#########################################################################\n'+
	'########################### Orientation #################################\n'+ 
	'#########################################################################\n')



CreateDIR('CentralGalaxy/Plots/Orientation')


A=[];B=[];C=[];D=[];E=[];F=[]
for i,j in zip(snaps,range(len(snaps))):
	A.append([]);B.append([]);C.append([]);D.append([]);E.append([]);F.append([])
	A[j]=theta(AngularMomentum_CW[i][:].T,AngularMomentum_Sph[i][:],mode=1)
	B[j]=theta(AngularMomentum_CW[i][:].T,AngularMomentum_Disk[i][:],mode=1)
	C[j]=theta(AngularMomentum_Sph[i][:].T,AngularMomentum_Disk[i][:],mode=1)
	D[j]=theta(AngularMomentum_CW[i][:].T,AngularMomentum_CG[i][:],mode=1)
	E[j]=theta(AngularMomentum_CG[i][:].T,AngularMomentum_Disk[i][:],mode=1)
	F[j]=theta(AngularMomentum_CG[i][:].T,AngularMomentum_Sph[i][:],mode=1)
A=np.array(A);B=np.array(B); C=np.array(C); D=np.array(D)

plotTheta(A,B,'Spheroid & Cosmic Web','Disk & Cosmic Web',redshift,snaps,'Disk_Spheroid_CW','Orientation between angular momentums ')
plotTheta(C,D,'Disk & Spheroid','Cosmics Web & Central Galaxy',redshift,snaps,'All','Orientation between angular momentums ')
plotTheta(E,F,'Disk & Central Galaxy','Spheroid & Central Galaxy',redshift,snaps,'Galaxy','Orientation between angular momentums ')

A=[];B=[];C=[];D=[];

for i,j in zip(snaps,range(len(snaps))):
	A.append([]);B.append([]);C.append([]);D.append([]);E.append([]);F.append([])
	A[j]=theta(AngularMomentum_CW[i][:].T,eigenvectors_CW[i][:,0])
	B[j]=theta(AngularMomentum_CG[i][:].T,eigenvectors_CG[i][:,2])
	C[j]=theta(AngularMomentum_Sph[i][:].T,eigenvectors_Sph[i][:,2])
	D[j]=theta(AngularMomentum_Disk[i][:].T,eigenvectors_Disk[i][:,2])
	
A=np.array(A);B=np.array(B); C=np.array(C); D=np.array(D)

plotTheta(A,C,'Cosmic Web','Galaxy',redshift,snaps,'CW_SPh_AngularAndTI','Angle between orientation and angular momentum ')
plotTheta(D,B,'Disk','CG',redshift,snaps,'Disk_CG_AngularAndTI','Angle between orientation and angular momentum ')

A=[];
for i,j in zip(snaps,range(len(snaps))):
	A.append([]);
	A[j]=theta(AngularMomentum_Sph[i][:].T,AngularMomentum_Disk[i][:],mode=1)
	
A=np.array(A);

plotThetaONE(A,'SPH & Disk',redshift,snaps,'SPH_DISK_angular','Angle between angular momentum of the disk and the spheroid ')



A=[];B=[];C=[];D=[];E=[];F=[]
for i,j in zip(snaps,range(len(snaps))):
	A.append([]);B.append([]);C.append([]);D.append([]);E.append([]);F.append([])
	A[j]=theta(eigenvectors_CW[i][:,0].T,eigenvectors_CG[i][:,2])
	B[j]=theta(eigenvectors_CW[i][:,0].T,eigenvectors_Disk[i][:,2])
	C[j]=theta(eigenvectors_CW[i][:,0].T,eigenvectors_Sph[i][:,2])
	D[j]=theta(eigenvectors_CG[i][:,2].T,eigenvectors_Disk[i][:,2])
	E[j]=theta(eigenvectors_CG[i][:,2].T,eigenvectors_Sph[i][:,2])
	F[j]=theta(eigenvectors_Disk[i][:,2].T,eigenvectors_Sph[i][:,2])
A=np.array(A);B=np.array(B); C=np.array(C); D=np.array(D)

plotTheta(A,F,'Central Galaxy & Cosmic Web','Disk & Spheroid',redshift,snaps,'IT_DiskSpheroid_CWCG','Orientation between Inertia Tensors eigenvector ')
plotTheta(B,C,'Disk & Cosmic Web','Spheroid & Cosmic Web',redshift,snaps,'IT_AllCW','Orientation between Inertia Tensors eigenvector ')
plotTheta(E,D,'Spheroid & Central Galaxy','Disk & Central Galaxy',redshift,snaps,'IT_Galaxy','Orientation between Inertia Tensors eigenvector ')




opcion=''
while str(opcion)!='no' and str(opcion)!='yes':
	opcion=input('Do you want plot the eigenvectors with the structures?...(yes/no): ')
print('Answer: {} .Ok'.format(opcion))

if opcion=='yes':
	CreateDIR('CentralGalaxy/Plots/Eigenvectors')
	CreateDIR('CentralGalaxy/Plots/Eigenvectors/Disk')
	CreateDIR('CentralGalaxy/Plots/Eigenvectors/Sph')
	CreateDIR('CentralGalaxy/Plots/Eigenvectors/CW')
	CreateDIR('CentralGalaxy/Plots/Eigenvectors/CG')
	Progress = ChargingBar('Plotting...', max=len(snaps))
	for j,i in zip(snaps,range(len(snaps))):
		i=int(i)
		salida='None'
		time.sleep(random.uniform(0, 0.2))
		Progress.next()
		plotVP(redshift[i],snaps[i],save_EVCDisk,Disk_Snaps_DataDF[j],CM_Disk[i],'Disk',60-i,salida)
		plotVP(redshift[i],snaps[i],save_EVCSph,Sph_Snaps_DataDF[j],CM_Sph[i],'Sph',60-i,salida)
		plotVP(redshift[i],snaps[i],save_EVCG,Snaps_DataDF[j],CM_CG[i],'CG',60-i,salida)
		plotVP(redshift[i],snaps[i],save_EVCW,CW_SnapsDataDF[j],CM_CW[i],'CW',60-i,salida)
	Progress.finish()

	print('New plots. Check CentralGalaxy/Plots/Orientation & CentralGalaxy/Plots/Eigenvectors')

CreateDIR('CentralGalaxy/Plots/Virial')

masssystem=[];masssph=[];massdisk=[];massgas=[]
"""
for j,i in zip(snaps, range(len(snaps))):
	r_vir=128.10*10**3*0.7 #pc 
	i=int(i)
	header=pd.read_csv('d5004/HEADER/'+j+'.csv')
	convV=f_convV(header['h0t0'][0],H0,header['h100'][0],header['box100'][0]/header['h100'][0],Mpc,yr,header['atime'][0],header['L'][0],header['padding'][0])
	convL=f_convL(header['box100'][0]/header['h100'][0],Mpc,header['atime'][0],header['L'][0],header['padding'][0])
	r_vir=r_vir*10**(-6)/convL #unidades del sistema
	#print('{}::{} : Parámetros de conversión: convV= {} y convL= {}, r_vir= {}'.format(i,j,convV,convL,r_vir))
	radius=(Snaps_DataDF[j]['rx']-CM_CG[i,0])**2+(Snaps_DataDF[j]['ry']-CM_CG[i,1])**2+(Snaps_DataDF[j]['rz']-CM_CG[i,2])**2
	radius=radius**(1/2)
	
	buf_mass=Snaps_DataDF[j][radius<=r_vir]; masa_rvir=buf_mass['m'].sum();convMass=1863506891.58/1e10; 
	buf_sph=buf_mass.loc[(buf_mass['Component']==3)] ; buf_sph=buf_sph['m'].sum()
	buf_disk=buf_mass.loc[(buf_mass['Component']==2) | (buf_mass['Component']==1) | (buf_mass['Component']==0)]; buf_disk=buf_disk['m'].sum()
	buf_gas=buf_mass.loc[(buf_mass['Component']==0)]; buf_gas=buf_gas['m'].sum()
	masa_rvir=masa_rvir*convMass #10¹0 masas solares
	masssystem.append(masa_rvir); masssph.append(buf_sph*convMass); massdisk.append(buf_disk*convMass); massgas.append(buf_gas*convMass)

R=plt.figure(figsize=(13.0, 10.0))
ax=R.add_subplot(111)	
longit=np.round(np.linspace(0,len(snaps)-1,len(snaps))); longit2=np.round(np.linspace(0,120,61))
longit=longit2
buf=np.array(list(masssystem)); masssph=np.array(list(masssph)); massdisk=np.array(list(massdisk)); massgas=np.array(list(massgas))
buf1=buf; masssph1=masssph;massdisk1=massdisk ; massgas1=massgas

plt.bar(longit[3:],buf1[3:],color='blue',width=1.5,label='Masa acretada')
plt.bar(longit[3:],masssph1[3:],color='red',width=1.5,label='Masa acretada esferoidal')
plt.bar(longit[3:],massdisk1[3:],color='black',width=1.5,label='Masa acretada disco')
plt.bar(longit[3:],massgas1[3:],color='magenta',width=1.5,label='Masa acretada gas contenida en el disco')
plt.legend()
plt.xticks(longit,np.round(redshift,3))
plt.xticks(rotation=90)
ax.set_ylabel('Mass',fontsize=25);ax.set_xlabel('Redshift',fontsize=25)
ax.set_title('Mass evolution',fontsize=25)
plt.savefig('CentralGalaxy/Plots/Virial/MassAccreted.pdf', bbox_inches = 'tight')

R=plt.figure(figsize=(13.0, 10.0))
ax=R.add_subplot(111)	
longit=np.round(np.linspace(0,len(snaps)-1,len(snaps))); longit2=np.round(np.linspace(0,120,61))
longit=longit2
buf=np.array(list(masssystem)); masssph=np.array(list(masssph)); massdisk=np.array(list(massdisk)); massgas=np.array(list(massgas))
buf1=buf/buf[60]; masssph1=masssph/masssph[60];massdisk1=massdisk/massdisk[60] ; massgas1=massgas/massgas[60]

plt.bar(longit[3:],masssph1[3:],color='black',width=1.5,label='Masa acretada esferoidal')
plt.bar(longit[3:],massdisk1[3:],color='darkgoldenrod',width=1.5,label='Masa acretada disco')
plt.bar(longit[3:],massgas1[3:],color='silver',width=1.5,label='Masa gas acretada contenida en el disco')
ax.set_ylabel('Mass/Mass(z=0)',fontsize=25)
plt.legend()
plt.xticks(longit,np.round(redshift,3))
plt.xticks(rotation=90)
ax.set_xlabel('Redshift',fontsize=25)
ax.set_title('Mass evolution',fontsize=25)

axes2 = plt.twinx()
axes2.plot(longit[3:],d[3:],linestyle='-',marker='o',markersize=4,color='red',label='Angular momentum Sph')
axes2.plot(longit[3:],c[3:],linestyle='-',marker='o',markersize=4,color='blue',label='Angular momentum Disco')

axes2.set_ylabel('Magnitude of the Angular momentum',fontsize=25)
plt.legend(loc="lower right")
plt.savefig('CentralGalaxy/Plots/Virial/MassAccreted2.pdf', bbox_inches = 'tight')

R=plt.figure(figsize=(13.0, 10.0))
ax=R.add_subplot(111)	
longit=np.round(np.linspace(0,len(snaps)-1,len(snaps))); longit2=np.round(np.linspace(0,120,61))
longit=longit2
buf=np.array(list(masssystem)); masssph=np.array(list(masssph)); massdisk=np.array(list(massdisk)); massgas=np.array(list(massgas))
buf1=buf/buf[60]; masssph1=masssph/masssph[60];massdisk1=massdisk/massdisk[60] ; massgas1=massgas/massgas[60]

plt.bar(longit[3:],masssph1[3:],color='black',width=1.5,label='Masa acretada esferoidal')
plt.bar(longit[3:],massdisk1[3:],color='darkgoldenrod',width=1.5,label='Masa acretada disco')
plt.bar(longit[3:],massgas1[3:],color='silver',width=1.5,label='Masa gas acretada contenida en el disco')
ax.set_ylabel('Mass/Mass(z=0)',fontsize=25)
plt.legend(loc="lower left")
plt.xticks(longit,np.round(redshift,3))
plt.xticks(rotation=90)
ax.set_xlabel('Redshift',fontsize=25)
ax.set_title('Mass evolution',fontsize=25)

axes2 = plt.twinx()
axes2.plot(longit[3:],B[3:],linestyle='-',marker='o',markersize=4,color='blue',label='Orientación Disco ')
axes2.plot(longit[3:],C[3:],linestyle='-',marker='o',markersize=4,color='red',label='Orientación SPH')

axes2.set_ylabel('Orientation',fontsize=25)
plt.legend(loc="lower right")
plt.savefig('CentralGalaxy/Plots/Virial/MassAccreted3.pdf', bbox_inches = 'tight')
print('Total Time: {}'.format(datetime.datetime.now() - begin_time))
"""
print('\n------Finished: Particles of the components of the central galaxy------\n')
print('____________________________________________________________by Víctor.R.P')

