##############################
from Packages import *
from Def_ReadAndSave import *
from Def_CentralGalaxy import *
from InertiaTensor import *
from AngularMomentum import *
##############################

def theta2(v, w,e2): 
	ang= np.abs(np.dot(w,v))
	
	return(ang)


def tomatrix(matrix,star,end):
	matrix=matrix.to_numpy()
	matrix=matrix[:,star:end]
	return matrix
def Rshape(a,b,i,absoluto=0):
	if int(i)==60:
		i=59
	if absoluto==0:
		return (np.array(a[i].reshape(3,1),dtype=np.float64)), (np.array(b[i+1].reshape(1,3),dtype=np.float64))
	if absoluto==1:
		return (np.array(a[i].reshape(3,1),dtype=np.float64)), (np.array(b[i+1].reshape(1,3),dtype=np.float64))

def plotTheta2(Y1,Y2,Y3,label1,label2,label3,redshift,snaps,name,title):
	R=plt.figure(figsize=(13.0, 10.0));ax=R.add_subplot(111)
	longit=np.round(np.linspace(0,len(snaps),len(snaps)))
	plt.plot(longit,Y1,'--o',color='green',label=label1)
	plt.plot(longit,Y2,color='blue',label=label2)
	plt.plot(longit,Y3,color='red',label=label3)

	plt.legend(fontsize=20)
	plt.title(title,fontsize=25); ax.set_ylabel('cos(A)',fontsize=20)
	ax.set_xlabel('Redshift',fontsize=20)

	plt.xticks(longit,np.round(np.flip(redshift),3));plt.xticks(rotation=90)
	plt.savefig('CentralGalaxy/Values_eigenvalues/'+name+'.pdf', bbox_inches = 'tight')

	plt.close()



def VectorQuiver(component,redshift,snaps,CM,dataframe,i):
	x1,x2,x3=np.array(CM['CMx'])[i],np.array(CM['CMy'])[i],np.array(CM['CMz'])[i]
	fig = plt.figure(figsize=(13.0, 10.0))
	ax = fig.gca(projection='3d')
	plt.title(component+'; Redshift {}'.format(round(redshift[i],3)),fontsize=25)
	ax.quiver(x1, x2, x3,(dataframe['eVec1_Minor'][i]),(dataframe['eVec2_Minor'][i]),(dataframe['eVec3_Minor'][i]), color=['r'],length=0.01, normalize=True,label='Menor')
	ax.quiver(x1, x2, x3,(dataframe['eVec1_Medium'][i]), (dataframe['eVec2_Medium'][i]), (dataframe['eVec3_Medium'][i]), color=['b'],length=0.01, normalize=True,label='Mediano')
	ax.quiver(x1, x2, x3,(dataframe['eVec1_Maximum'][i]), (dataframe['eVec2_Maximum'][i]), (dataframe['eVec3_Maximum'][i]), color=['k'],length=0.01, normalize=True,label='Mayor')
	ax.legend()
	ax.set_xlabel('X',fontsize=20);ax.set_ylabel('Y',fontsize=20);ax.set_zlabel('Z',fontsize=20)
	ax.view_init(elev=20., azim=130)

	plt.savefig('CentralGalaxy/Plots/Eigenvectors/'+component+'/'+snaps[i]+'.pdf', bbox_inches = 'tight')
	plt.close()


def quiv3(ax,CM,a,i):
	x,y,z=np.array(CM['CMx'])[i],np.array(CM['CMy'])[i],np.array(CM['CMz'])[i]
	ax.quiver(x, y, z,(a['eVec1_Minor'][i]),(a['eVec2_Minor'][i]),(a['eVec3_Minor'][i]), color=['r'],length=0.001, normalize=True)
	ax.quiver(x, y, z,(a['eVec1_Medium'][i]), (a['eVec2_Medium'][i]), (a['eVec3_Medium'][i]), color=['b'],length=0.001, normalize=True)
	ax.quiver(x, y, z,(a['eVec1_Maximum'][i]), (a['eVec2_Maximum'][i]), (a['eVec3_Maximum'][i]), color=['k'],length=0.001, normalize=True)


def VectorQuiverALL(component,redshift,snaps,CM1,CM2,CM3,CM4,dataframe1,dataframe2,dataframe3,dataframe4,i):
	fig = plt.figure(figsize=(13.0, 10.0))
	ax = fig.gca(projection='3d')
	plt.title(component+'; Redshift {}'.format(round(redshift[i],3)),fontsize=25)

	quiv3(ax,CM1,dataframe1,i)
	quiv3(ax,CM2,dataframe2,i)
	quiv3(ax,CM3,dataframe3,i)
	quiv3(ax,CM4,dataframe4,i)

	ax.set_xlabel('X',fontsize=20);ax.set_ylabel('Y',fontsize=20);ax.set_zlabel('Z',fontsize=20)
	ax.view_init(elev=20., azim=30)

	plt.savefig('CentralGalaxy/Plots/Eigenvectors/'+component+'/'+snaps[i]+'.pdf', bbox_inches = 'tight')
	plt.close()

fileDir = r"./CentralGalaxy/CM_DATA"
fileExt = r".csv"
files=[a for a in os.listdir(fileDir) if a.endswith(fileExt)]
files.sort()

CM_G = pd.read_csv(fileDir+'/'+files[0])
CM_W = pd.read_csv(fileDir+'/'+files[1])
CM_Disk = pd.read_csv(fileDir+'/'+files[2])
CM_Sph = pd.read_csv(fileDir+'/'+files[3])



snaps,root=ListData()
redshift=np.loadtxt('CentralGalaxy/redshift_5004.dat'); redshift=redshift[:,2];redshift=np.flip(redshift)
longit=np.round(np.linspace(0,len(snaps),len(snaps)))


disk=pd.read_csv('CentralGalaxy/Values_eigenvalues/Disk.txt',sep=' ',index_col=0)
sph=pd.read_csv('CentralGalaxy/Values_eigenvalues/Spheroid.txt',sep=' ',index_col=0)
cw=pd.read_csv('CentralGalaxy/Values_eigenvalues/CW.txt',sep=' ',index_col=0)
cg=pd.read_csv('CentralGalaxy/Values_eigenvalues/CG.txt',sep=' ',index_col=0)



matrix_disk_min=tomatrix(disk,5,8); matrix_disk_med=tomatrix(disk,8,11);matrix_disk_sup=tomatrix(disk,11,14)
matrix_sph_min=tomatrix(sph,5,8);matrix_sph_med=tomatrix(sph,8,11);matrix_sph_sup=tomatrix(sph,11,14)
matrix_cw_min=tomatrix(cw,5,8);matrix_cw_med=tomatrix(cw,8,11);matrix_cw_sup=tomatrix(cw,11,14)
matrix_cg_min=tomatrix(cg,5,8);matrix_cg_med=tomatrix(cg,8,11);matrix_cg_sup=tomatrix(cg,11,14)


A=[]; B=[]; C=[]; D= []
"""
CreateDIR('CentralGalaxy/Plots/Eigenvectors')
CreateDIR('CentralGalaxy/Plots/Eigenvectors/Disk')
CreateDIR('CentralGalaxy/Plots/Eigenvectors/Sph')
CreateDIR('CentralGalaxy/Plots/Eigenvectors/CW')
CreateDIR('CentralGalaxy/Plots/Eigenvectors/CG')
"""
CreateDIR('CentralGalaxy/Plots/Eigenvectors/All')

med_A=[]; med_B=[]; med_C=[]; med_D= []
sup_A=[]; sup_B=[]; sup_C=[]; sup_D= []
opcion=input('...1 or 2....: ')

if int(opcion)==1:

	for i in range(len(longit)):	

		buf,buf1=Rshape(matrix_disk_med,matrix_disk_min,i)
		buf2,buf3=Rshape(matrix_sph_med,matrix_sph_min,i)
		buf4,buf5=Rshape(matrix_cw_med,matrix_cw_min,i)
		buf6,buf7=Rshape(matrix_cg_med,matrix_cg_min,i)

		med_buf,med_buf1=Rshape(matrix_disk_sup,matrix_disk_med,i)
		med_buf2,med_buf3=Rshape(matrix_sph_sup,matrix_sph_med,i)
		med_buf4,med_buf5=Rshape(matrix_cw_sup,matrix_cw_med,i)
		med_buf6,med_buf7=Rshape(matrix_cg_sup,matrix_cg_med,i)

		sup_buf,sup_buf1=Rshape(matrix_disk_sup,matrix_disk_min,i,1)
		sup_buf2,sup_buf3=Rshape(matrix_sph_sup,matrix_sph_min,i,1)
		sup_buf4,sup_buf5=Rshape(matrix_cw_sup,matrix_cw_min,i,1)
		sup_buf6,sup_buf7=Rshape(matrix_cg_sup,matrix_cg_min,i,1)

	  	
		#VectorQuiver('Disk',redshift,snaps,CM_Disk,disk,i)
		#VectorQuiver('Sph',redshift,snaps,CM_Sph,sph,i)
		#VectorQuiver('CW',redshift,snaps,CM_W,cw,i)
		#VectorQuiver('CG',redshift,snaps,CM_G,cg,i)

		VectorQuiverALL('All',redshift,snaps,CM_Disk,CM_Sph,CM_W,CM_G,disk,sph,cw,cg,i)


		A.append(theta2(buf,buf1,med_buf1)[0]);B.append(theta2(buf2,buf3,med_buf3)[0]);
		C.append(theta2(buf4,buf5,med_buf5)[0]);D.append(theta2(buf6,buf7,med_buf7)[0])

		med_A.append(theta2(med_buf,med_buf1,buf1)[0]);med_B.append(theta2(med_buf2,med_buf3,buf3)[0]);
		med_C.append(theta2(med_buf4,med_buf5,buf5)[0]);med_D.append(theta2(med_buf6,med_buf7,buf7)[0])

		sup_A.append(theta2(sup_buf,sup_buf1,med_buf1)[0]);sup_B.append(theta2(sup_buf2,sup_buf3,med_buf3)[0]);
		sup_C.append(theta2(sup_buf4,sup_buf5,med_buf5)[0]);sup_D.append(theta2(sup_buf6,sup_buf7,sup_buf7)[0])



	plotTheta2(A,med_A,sup_A,'e1*e2(0)','e2*e3(0)','e1*e3(0)',redshift,snaps,'DISK_cruzado','e_{i,t}*e_0')
	plotTheta2(B,med_B,sup_B,'e1*e2(0)','e2*e3(0)','e1*e3(0)',redshift,snaps,'SPH_cruzado','e_{i,t}*e_0')
	plotTheta2(C,med_C,sup_C,'e1*e2(0)','e2*e3(0)','e1*e3(0)',redshift,snaps,'CW_cruzado','e_{i,t}*e_0')
	plotTheta2(D,med_D,sup_D,'e1*e2(0)','e2*e3(0)','e1*e3(0)',redshift,snaps,'CG_cruzado','e_{i,t}*e_0')

if int(opcion)==2:
	for i in range(len(longit)):
		buf,buf1=Rshape(matrix_disk_min,matrix_disk_min,i)
		buf2,buf3=Rshape(matrix_sph_min,matrix_sph_min,i)
		buf4,buf5=Rshape(matrix_cw_min,matrix_cw_min,i)
		buf6,buf7=Rshape(matrix_cg_min,matrix_cg_min,i)

		med_buf,med_buf1=Rshape(matrix_disk_med,matrix_disk_med,i)
		med_buf2,med_buf3=Rshape(matrix_sph_med,matrix_sph_med,i)
		med_buf4,med_buf5=Rshape(matrix_cw_med,matrix_cw_med,i)
		med_buf6,med_buf7=Rshape(matrix_cg_med,matrix_cg_med,i)

		sup_buf,sup_buf1=Rshape(matrix_disk_sup,matrix_disk_sup,i,1)
		sup_buf2,sup_buf3=Rshape(matrix_sph_sup,matrix_sph_sup,i,1)
		sup_buf4,sup_buf5=Rshape(matrix_cw_sup,matrix_cw_sup,i,1); 
		sup_buf6,sup_buf7=Rshape(matrix_cg_sup,matrix_cg_sup,i,1); 

	  	
		#VectorQuiver('Disk',redshift,snaps,CM_Disk,disk,i)
		#VectorQuiver('Sph',redshift,snaps,CM_Sph,sph,i)
		#VectorQuiver('CW',redshift,snaps,CM_W,cw,i)
		#VectorQuiver('CG',redshift,snaps,CM_G,cg,i)

		VectorQuiverALL('All',redshift,snaps,CM_Disk,CM_Sph,CM_W,CM_G,disk,sph,cw,cg,i)

		A.append(theta2(buf,buf1,med_buf1)[0]);B.append(theta2(buf2,buf3,med_buf3)[0]);
		C.append(theta2(buf4,buf5,med_buf5)[0]);D.append(theta2(buf6,buf7,med_buf7)[0])

		med_A.append(theta2(med_buf,med_buf1,buf1)[0]);med_B.append(theta2(med_buf2,med_buf3,buf3)[0]);
		med_C.append(theta2(med_buf4,med_buf5,buf5)[0]);med_D.append(theta2(med_buf6,med_buf7,buf7)[0])

		sup_A.append(theta2(sup_buf,sup_buf1,sup_buf1)[0]);sup_B.append(theta2(sup_buf2,sup_buf3,sup_buf3)[0]);
		sup_C.append(theta2(sup_buf4,sup_buf5,sup_buf5)[0]);sup_D.append(theta2(sup_buf6,sup_buf7,sup_buf7)[0])
	plotTheta2(A,med_A,sup_A,'e1(t+1)*e1(t)','e2(t+1)*e2(t)','e3(t+1)*e3(t)',redshift,snaps,'DISK','e_{i,t}*e_0')
	plotTheta2(B,med_B,sup_B,'e1(t+1)*e1(t)','e2(t+1)*e2(t)','e3(t+1)*e3(t)',redshift,snaps,'SPH','e_{i,t}*e_0')
	plotTheta2(C,med_C,sup_C,'e1(t+1)*e1(t)','e2(t+1)*e2(t)','e3(t+1)*e3(t)',redshift,snaps,'CW','e_{i,t}*e_0')
	plotTheta2(D,med_D,sup_D,'e1(t+1)*e1(t)','e2(t+1)*e2(t)','e3(t+1)*e3(t)',redshift,snaps,'CG','e_{i,t}*e_0')

def mag(x):
	return(np.sqrt(x.dot(x)))

mod1=[]; mod2=[]; mod3=[]

mag1 = np.array(sph[["eVec1_Minor", "eVec2_Minor", "eVec3_Minor"]])
mag2 = np.array(sph[["eVec1_Medium", "eVec2_Medium", "eVec3_Medium"]])
mag3 = np.array(sph[["eVec1_Maximum", "eVec2_Maximum", "eVec3_Maximum"]])

for i in range(61):
	b1 = mag(mag1[i,:]-mag3[i,:])
	b2 = mag(mag2[i,:]-mag3[i,:])
	b3 = mag(mag3[i,:])
	mod1.append(b1); mod2.append(b2); mod3.append(b3)

mod1=np.array(mod1);mod2=np.array(mod2)
R=plt.figure(figsize=(13.0, 10.0))
ax=R.add_subplot(111)
plt.plot(longit,np.absolute(mod2),'o',color='blue',label='mediano-Maximo');
plt.plot(longit,np.absolute(mod1),'o',color='red',label='maximo-menor');
plt.ylim([0,10])
plt.grid()
plt.xticks(longit,np.round(redshift,3))
plt.xticks(rotation=90)
plt.legend()
plt.savefig('CentralGalaxy/Values_eigenvalues/sphdiferencia.png')

plt.close()
"""
R=plt.figure(figsize=(13.0, 10.0))
ax=R.add_subplot(111)
plt.plot(longit,np.absolute(sph['eVal_Minor']-sph['eVal_Medium']),'o',color='blue',label='Menor-Mediano');
plt.plot(longit,np.absolute(sph['eVal_Medium']-sph['eVal_Maximum']),'o',color='red',label='Mediano-Maximo');
plt.ylim([0,10])

plt.grid()
plt.legend()

plt.xticks(longit,np.round(redshift,3))
plt.xticks(rotation=90)
plt.savefig('CentralGalaxy/Values_eigenvalues/sph.png')

plt.close()
R=plt.figure(figsize=(13.0, 10.0))
ax=R.add_subplot(111)
plt.plot(longit,np.absolute(cg['eVal_Minor']-cg['eVal_Medium']),'o',color='blue',label='Menor-Mediano');
plt.plot(longit,np.absolute(cg['eVal_Medium']-cg['eVal_Maximum']),'o',color='red',label='Mediano-Maximo');
plt.legend()
plt.grid()
plt.xticks(longit,np.round(redshift,3))
plt.xticks(rotation=90)
plt.ylim([0,10])
plt.savefig('CentralGalaxy/Values_eigenvalues/cg.png')

plt.close()
R=plt.figure(figsize=(13.0, 10.0))
ax=R.add_subplot(111)
plt.plot(longit,np.absolute(cw['eVal_Minor']-cw['eVal_Medium']),'o',color='blue',label='Menor-Mediano');
plt.plot(longit,np.absolute(cw['eVal_Medium']-cw['eVal_Maximum']),'o',color='red',label='Mediano-Maximo');
plt.grid()
plt.legend()
plt.ylim([0,10])

plt.xticks(longit,np.round(redshift,3))
plt.xticks(rotation=90)
plt.savefig('CentralGalaxy/Values_eigenvalues/cw.png')

plt.close()
"""




"""
for i in range(len(longit)):	
	buf,buf1=Rshape(matrix_disk_med,matrix_disk_min,i)
	buf2,buf3=Rshape(matrix_sph_med,matrix_sph_min,i)
	buf4,buf5=Rshape(matrix_cw_med,matrix_cw_min,i)
	buf6,buf7=Rshape(matrix_cg_med,matrix_cg_min,i)

	med_buf,med_buf1=Rshape(matrix_disk_sup,matrix_disk_med,i)
	med_buf2,med_buf3=Rshape(matrix_sph_sup,matrix_sph_med,i)
	med_buf4,med_buf5=Rshape(matrix_cw_sup,matrix_cw_med,i)
	med_buf6,med_buf7=Rshape(matrix_cg_sup,matrix_cg_med,i)

	sup_buf,sup_buf1=Rshape(matrix_disk_med,matrix_disk_sup,i)
	sup_buf2,sup_buf3=Rshape(matrix_sph_med,matrix_sph_sup,i)
	sup_buf4,sup_buf5=Rshape(matrix_cw_med,matrix_cw_sup,i)
	sup_buf6,sup_buf7=Rshape(matrix_cg_med,matrix_cg_sup,i)

  	
	VectorQuiver('Disk',redshift,snaps,CM_Disk,disk,i)
	VectorQuiver('Sph',redshift,snaps,CM_Sph,sph,i)
	VectorQuiver('CW',redshift,snaps,CM_W,cw,i)
	VectorQuiver('CG',redshift,snaps,CM_G,cg,i)

	VectorQuiverALL('All',redshift,snaps,CM_Disk,CM_Sph,CM_W,CM_G,disk,sph,cw,cg,i)

	A.append(theta2(buf,buf1)[0]);B.append(theta2(buf2,buf3)[0]);
	C.append(theta2(buf4,buf5)[0]);D.append(theta2(buf6,buf7)[0])

	med_A.append(theta2(med_buf,med_buf1)[0]);med_B.append(theta2(med_buf2,med_buf3)[0]);
	med_C.append(theta2(med_buf4,med_buf5)[0]);med_D.append(theta2(med_buf6,med_buf7)[0])

	sup_A.append(theta2(sup_buf,sup_buf1)[0]);sup_B.append(theta2(sup_buf2,sup_buf3)[0]);
	sup_C.append(theta2(sup_buf4,sup_buf5)[0]);sup_D.append(theta2(sup_buf6,sup_buf7)[0])



plotTheta2(A,med_A,sup_A,'e1*e2(0)','e2*e3(0)','e3*e2(0)',redshift,snaps,'DISK_cruzado','e_{i,t}*e_0')
plotTheta2(B,med_B,sup_B,'e1*e2(0)','e2*e3(0)','e3*e2(0)',redshift,snaps,'SPH_cruzado','e_{i,t}*e_0')
plotTheta2(C,med_C,sup_C,'e1*e2(0)','e2*e3(0)','e3*e2(0)',redshift,snaps,'CW_cruzado','e_{i,t}*e_0')
plotTheta2(D,med_D,sup_D,'e1*e2(0)','e2*e3(0)','e3*e2(0)',redshift,snaps,'CG_cruzado','e_{i,t}*e_0')


	buf,buf1=Rshape(matrix_disk_min,matrix_disk_min,i)
	buf2,buf3=Rshape(matrix_sph_min,matrix_sph_min,i)
	buf4,buf5=Rshape(matrix_cw_min,matrix_cw_min,i)
	buf6,buf7=Rshape(matrix_cg_min,matrix_cg_min,i)

	med_buf,med_buf1=Rshape(matrix_disk_med,matrix_disk_med,i)
	med_buf2,med_buf3=Rshape(matrix_sph_med,matrix_sph_med,i)
	med_buf4,med_buf5=Rshape(matrix_cw_med,matrix_cw_med,i)
	med_buf6,med_buf7=Rshape(matrix_cg_med,matrix_cg_med,i)

	sup_buf,sup_buf1=Rshape(matrix_disk_sup,matrix_disk_sup,i)
	sup_buf2,sup_buf3=Rshape(matrix_sph_sup,matrix_sph_sup,i)
	sup_buf4,sup_buf5=Rshape(matrix_cw_sup,matrix_cw_sup,i)
	sup_buf6,sup_buf7=Rshape(matrix_cg_sup,matrix_cg_sup,i)

  	
	VectorQuiver('Disk',redshift,snaps,CM_Disk,disk,i)
	VectorQuiver('Sph',redshift,snaps,CM_Sph,sph,i)
	VectorQuiver('CW',redshift,snaps,CM_W,cw,i)
	VectorQuiver('CG',redshift,snaps,CM_G,cg,i)

	VectorQuiverALL('All',redshift,snaps,CM_Disk,CM_Sph,CM_W,CM_G,disk,sph,cw,cg,i)

	A.append(theta2(buf,buf1)[0]);B.append(theta2(buf2,buf3)[0]);
	C.append(theta2(buf4,buf5)[0]);D.append(theta2(buf6,buf7)[0])

	med_A.append(theta2(med_buf,med_buf1)[0]);med_B.append(theta2(med_buf2,med_buf3)[0]);
	med_C.append(theta2(med_buf4,med_buf5)[0]);med_D.append(theta2(med_buf6,med_buf7)[0])

	sup_A.append(theta2(sup_buf,sup_buf1)[0]);sup_B.append(theta2(sup_buf2,sup_buf3)[0]);
	sup_C.append(theta2(sup_buf4,sup_buf5)[0]);sup_D.append(theta2(sup_buf6,sup_buf7)[0])



plotTheta2(A,med_A,sup_A,'e1*e1(0)','e2*e2(0)','e3*e3(0)',redshift,snaps,'DISK','e_{i,t}*e_0')
plotTheta2(B,med_B,sup_B,'e1*e1(0)','e2*e2(0)','e3*e3(0)',redshift,snaps,'SPH','e_{i,t}*e_0')
plotTheta2(C,med_C,sup_C,'e1*e1(0)','e2*e2(0)','e3*e3(0)',redshift,snaps,'CW','e_{i,t}*e_0')
plotTheta2(D,med_D,sup_D,'e1*e1(0)','e2*e2(0)','e3*e3(0)',redshift,snaps,'CG','e_{i,t}*e_0')

"""
