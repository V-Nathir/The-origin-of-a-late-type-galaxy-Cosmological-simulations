##############################
from Packages import *
from Def_ReadAndSave import *
from pyevtk.hl import pointsToVTK
##############################
#Dir=["d5004/HEADER","d5004/MRV","d5004/BAR"]
print('\n----Checkout: Reading and saving raw data----\n')

snaps,root=ListData()
print('\n-> Files found: {} \n-> Snaps:\n {}'.format(len(snaps),snaps))

Control=True
while Control==True:
	try:
		lendata=int(input('\n-> Enter the length of the list of data to be displayed (20 recommended): '))
		Control=False
	except ValueError: 
		Control=True
		print('-> The length must be an integer')

len_snaps=len(snaps)

print('\n-> Data from {}'.format(Dir[1]))
for i in range(len_snaps):
	print('\n  		- Snap: ||{}||'.format(snaps[i]) )
	try:
		Load=np.load((Dir[1]+'/'+snaps[i]+'.npy'))
		print(HeadMRV)
		print(Load[0:lendata])
	except FileNotFoundError: 
		input('\n-> File does not exist in {}: {}'.format(Dir[1],snaps[i]))
		Read_Save(Dir,root[i],snaps[i])
		print('-> File created\n')
		Load=np.load((Dir[1]+'/'+snaps[i]+'.npy'))
		print(HeadMRV)
		print(Load[0:lendata])
print('Data length: {}'.format(len(Load)))

Load = pd.DataFrame(Load,index=Load[:,0],columns= HeadMRV)
print('Data length stars: {}'.format(len(Load[Load['itype']==-1])))
print('Data length gas: {}'.format(len(Load[Load['itype']==1])))
print('Data length Dark Matter: {}'.format(len(Load[Load['itype']==0])))

Load_star = Load[Load['itype']==-1]
def plotParticles(data,alpha=0.5):
	plt.style.use('dark_background')

	figCM= plt.figure(figsize=(13.0, 10.0))
	ax=figCM.add_subplot(111,projection='3d')
	P =  data[data['itype']==0]
	ax.scatter(P['rx'],P['ry'],P['rz'],c='magenta',s=0.1, alpha=alpha,marker='o',label='Dark Matter')
	P =  data[data['itype']==-1]
	ax.scatter(P['rx'],P['ry'],P['rz'],c='white',s=0.1, alpha=alpha,marker='o',label='Stars')
	P =  data[data['itype']==1]
	ax.scatter(P['rx'],P['ry'],P['rz'],c='blue',s=0.1, alpha=alpha,marker='o',label='Gas')

	ax.grid(False)


	plt.legend(fontsize=15,markerscale=20)
	

	ax.set_xlabel('X')

	ax.set_ylabel('Y')
	ax.set_zlabel('Z')

	ax.view_init(elev=30, azim=70);	
	ax.view_init(elev=30,azim=250);	
	plt.show()
	plt.close()

plotParticles(Load,alpha=0.5)
x = Load_star['rx']; x = np.ascontiguousarray(x.to_numpy())
y = Load_star['ry']; y = np.ascontiguousarray(y.to_numpy())
z = Load_star['rz']; z = np.ascontiguousarray(z.to_numpy())
print(x)
vel = np.sqrt(Load_star['vx']**2+Load_star['vy']**2+Load_star['vz']**2)
vel = np.ascontiguousarray(vel.to_numpy())
print(vel)
pointsToVTK("./points", x, y, z, data = {"Mod.v" : vel})
DM = Load[Load['itype']==0]
print(DM.describe())

