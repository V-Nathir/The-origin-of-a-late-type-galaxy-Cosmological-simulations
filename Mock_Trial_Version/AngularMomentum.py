from Packages import * 


def AngularMomentum(data,CM):

	vx=data['vx']*data['m'];vy=data['vy']*data['m'];vz=data['vz']*data['m']
	mtot=data['m'].sum()

	vxCM=vx.sum()/mtot; vyCM=vy.sum()/mtot;vzCM=vz.sum()/mtot
	vCM=np.array([vxCM,vyCM,vzCM])

	position=np.stack([data['rx']-CM[0],data['ry']-CM[1],data['rz']-CM[2]]); position=position.T

	vParticle=np.stack( [ data['m']*(data['vx']-vCM[0]),data['m']*(data['vy']-vCM[1]),data['m']*(data['vz']-vCM[2])] );vParticle=vParticle.T

	vectorial1=position[:,1]*vParticle[:,2]-position[:,2]*vParticle[:,1]#i
	vectorial2=-(position[:,0]*vParticle[:,2]-position[:,2]*vParticle[:,0]) #j
	vectorial3=position[:,0]*vParticle[:,1]-position[:,1]*vParticle[:,0] #k

	vectorial=np.stack([vectorial1,vectorial2,vectorial3]); vectorial=vectorial.T;

	vectorial=sklearn.preprocessing.normalize(vectorial, norm="l1")

	vectorial=vectorial.sum(axis=0); 
	
	AngularMomentum=vectorial/len(np.array(data['m'])); 
	AngularMomentum=np.array(AngularMomentum)[np.newaxis]; AngularMomentum=AngularMomentum.T ;
	return(AngularMomentum)


