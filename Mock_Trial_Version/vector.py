##############################
from Packages import *
from Def_ReadAndSave import *
from Def_CentralGalaxy import *
from InertiaTensor import *
from AngularMomentum import *
##############################


def plotVP(redshift,snap,dataframe_vector,particles,CM,component,i,salida):
	x1,x2,x3=np.array(CM[0]),np.array(CM[1]),np.array(CM[2])
	fig = plt.figure(figsize=(13.0, 10.0))
	ax = fig.gca(projection='3d')
	plt.title(component+'; Redshift {}'.format(round(redshift,3)),fontsize=25)
	ax.quiver(0, 0, 0,dataframe_vector['eVec1_Minor'][i],dataframe_vector['eVec2_Minor'][i],dataframe_vector['eVec3_Minor'][i], color=['r'],length=0.0025, normalize=True,label='Menor')
	ax.quiver(0, 0, 0,dataframe_vector['eVec1_Medium'][i], dataframe_vector['eVec2_Medium'][i], dataframe_vector['eVec3_Medium'][i], color=['g'],length=0.0025, normalize=True,label='Mediano')
	ax.quiver(0, 0, 0,dataframe_vector['eVec1_Maximum'][i], dataframe_vector['eVec2_Maximum'][i], dataframe_vector['eVec3_Maximum'][i], color=['k'],length=0.0025, normalize=True,label='Mayor')

	ax.scatter(particles['rx']-x1,particles['ry']-x2,particles['rz']-x3,c='b',s=6, alpha=0.01,marker='o')
	if i>=57:
		ax.set_xlim([-0.0045,0.0045])
		ax.set_zlim([-0.0045,0.0045])
		ax.set_ylim([-0.0045,0.0045])
	if i<57 and i>44:
		ax.set_xlim([-0.004,0.004])
		ax.set_zlim([-0.004,0.004])
		ax.set_ylim([-0.004,0.004])
	if i<=44:
		ax.set_xlim([-0.003,0.003])
		ax.set_zlim([-0.003,0.003])
		ax.set_ylim([-0.003,0.003])
	ax.legend(loc='lower right')
	ax.set_xlabel('X',fontsize=20);ax.set_ylabel('Y',fontsize=20);ax.set_zlabel('Z',fontsize=20)
	ax.view_init(elev=20., azim=-30)

	plt.savefig('CentralGalaxy/Plots/Eigenvectors/'+component+'/'+snap+'.png', bbox_inches = 'tight')
	if salida==snap:
		plt.show()
	plt.close()

def plotVirial(redshift,snap,radio,particles,CM,component,salida):
	x1,x2,x3=np.array(CM[0]),np.array(CM[1]),np.array(CM[2])
	fig = plt.figure(figsize=(13.0, 10.0))
	ax = fig.gca(projection='3d')
	plt.title(component+'; Redshift {}'.format(round(redshift,3)),fontsize=25)
	ax.quiver(0, 0, 0,0,0,radio, color=['r'])
	ax.quiver(0, 0, 0,radio,0,0, color=['r'])
	ax.quiver(0, 0, 0,0,radio, 0, color=['r'])

	ax.scatter(particles['rx']-x1,particles['ry']-x2,particles['rz']-x3,c='b',s=6, alpha=0.01,marker='o')
	ax.set_xlim([-0.003,0.003])
	ax.set_zlim([-0.003,0.003])
	ax.set_ylim([-0.003,0.003])

	ax.set_xlabel('X',fontsize=20);ax.set_ylabel('Y',fontsize=20);ax.set_zlabel('Z',fontsize=20)
	ax.view_init(elev=20., azim=-30)

	plt.savefig('CentralGalaxy/Plots/Virial/'+snap+'.pdf', bbox_inches = 'tight')
	if salida==snap:
		plt.show()
	plt.close()