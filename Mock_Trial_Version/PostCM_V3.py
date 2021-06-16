##############################
from Packages import *
from Def_ReadAndSave import convert
##############################

def cube(data,xmin,xmax,ymin,ymax,zmin,zmax):
	dataframe=data[ (data['rx']>= xmin) & (data['rx']<= xmax) & 
	(data['ry']>= ymin) & (data['ry']<= ymax) & (data['rz']<= zmax) & (data['rz']>= zmin)]
	return(dataframe)
def radius_particle(DataFrame,snap,CM):
	New_rx=DataFrame[snap]['rx']-CM[0]
	New_ry=DataFrame[snap]['ry']-CM[1]
	New_rz=DataFrame[snap]['rz']-CM[2]

	return(np.sqrt(New_rx**2+New_ry**2+New_rz**2))

def radius_particle2(DataFrame,CM):
	New_rx=DataFrame['rx']-CM[0]
	New_ry=DataFrame['ry']-CM[1]
	New_rz=DataFrame['rz']-CM[2]

	return(np.sqrt(New_rx**2+New_ry**2+New_rz**2))

def PostCM(Snaps_DataDF,snap,CM,r_PostCM,r_sub,maxr_partin):

	radio   = r_PostCM  ; n_particles=10000
	onion = np.linspace(0.0,radio,3)
	while n_particles>= 4000:
		buf_onion = []
		r_CM = radius_particle(Snaps_DataDF, snap, CM)

		for i in range( len(onion ) ):
			if i == len(onion)-1:
				continue
			radio_u = onion[i+1] ; radio_d = onion[i]
			try:
				bufpart_in = Snaps_DataDF[snap][ r_CM>=radio_d];bufpart_in = bufpart_in[ r_CM<=radio_u];
				buf_onion.append( len(bufpart_in))
			except UserWarning:
				pass
		onion_it_max     = buf_onion.index(max(buf_onion))
		onion_boundaries = np.array([onion[onion_it_max], onion[onion_it_max+1]])

		radio_u     = onion_boundaries[1] ; radio_d = onion_boundaries[0]
		onion       = np.linspace(radio_d,radio_u,3)
		n_particles = max(buf_onion)
	onion_it_max     = buf_onion.index(max(buf_onion))
	onion_boundaries = np.array([onion[onion_it_max], onion[onion_it_max+1]])
	radio_u = onion_boundaries[1] ; radio_d = onion_boundaries[0]
	part_in = Snaps_DataDF[snap][r_CM>=radio_d];part_in = part_in[r_CM<=radio_u]; 
	droplist= part_in.index 
	alldata = Snaps_DataDF[snap].drop( droplist )
	vec_zero=np.zeros(len(part_in))
	part_in.insert(0, '7Mass',vec_zero,True)
	#print('{} :: N de particulas {} :: Radio {} [{},{}]'.format(snap,len(part_in), radio_u-radio_d,radio_d,radio_u))


	
	CM=Mass7(part_in,CM,r_sub,alldata,maxr_partin)
	
	return(CM)

def Mass7(part_in,CM,r_sub, alldata,maxr_partin):
	radio_p = r_sub 
	list_index=part_in.index
	for i in list_index:
		xyz       = np.array(part_in.loc[i, ['rx','ry','rz']])
		r_xyz     = radius_particle2(part_in, xyz)
		r_xyzall  = radius_particle2(alldata, xyz)

		try:
			part_in.at[i,'7Mass'] =  (part_in[r_xyz <= radio_p]['m'].sum() + 
			 	alldata[r_xyzall <= radio_p]['m'].sum() )
		
		except AttributeError: 
			part_in.at[i,'7Mass'] = 0

	part_max= part_in[ part_in['7Mass']==part_in['7Mass'].max()] ;
	indice_max=part_max.index
	try :
		indice_max=indice_max[0]
		CM=np.array(part_in.loc[indice_max, ['rx','ry','rz']])
		return(CM)
	except IndexError:
		return(CM)

#CUBE
"""
	zmax = part_in['rz'].max() ; zmin = part_in['rz'].min() ; zinter = (zmax+zmin)/2
	ymax = part_in['ry'].max() ; ymin = part_in['ry'].min() ; yinter = (ymax+ymin)/2
	xmax = part_in['rx'].max() ; xmin = part_in['rx'].min() ; xinter = (xmax+xmin)/2
	axiszcube= np.array([zmin,zinter,zmax]) ; axisycube=np.array( [ymin,yinter,ymax]) ; axisxcube = np.array([xmin,xinter,xmax])
	lenscubes=[]
	for cubox in range(2):
		i_x = axisxcube[cubox] ; f_x = axisxcube[cubox+1]
		for cuboy in range(2):
			i_y = axisycube[cuboy] ; f_y = axisycube[cuboy+1]
			for cuboz in range(2):
				i_z = axiszcube[cuboz] ; f_z = axiszcube[cuboz+1]
				buf_cube= cube(part_in,i_x,f_x,i_y,f_y,i_z,f_z)
				lenscubes.append(len(buf_cube))
	index_axiszcube= list([0,1,2]) ; index_axisycube=list( [0,1,2]) ; index_axisxcube = list([0,1,2])
	index_maxlencubes=lenscubes.index(max(lenscubes))
	count=0 ; now= 'go'
	for cubox in range(2):
		i_x = axisxcube[cubox] ; f_x = axisxcube[cubox+1]
		if now == 'stop':
			break
		for cuboy in range(2):
			i_y = axisycube[cuboy] ; f_y = axisycube[cuboy+1]
			if now == 'stop':
				break
			for cuboz in range(2):
				i_z = axiszcube[cuboz] ; f_z = axiszcube[cuboz+1]
				indices = np.array([i_x,f_x,i_y,f_y,i_z,f_z])
				if count == index_maxlencubes:
					now = 'stop'
					break
				count=count+1
	part_in = cube(part_in,indices[0],indices[1],indices[2],indices[3],indices[4],indices[5]) 
	"""