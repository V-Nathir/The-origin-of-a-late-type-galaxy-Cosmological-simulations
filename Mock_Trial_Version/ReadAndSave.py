##############################
from Packages import *
from Def_ReadAndSave import *
##############################
print('\n----Reading and saving raw data----')

snaps,root=ListData()
print('\n-> Files found: {} \n-> Snaps:\n {}'.format(len(snaps),snaps))

CreateDIR("d5004");CreateDIR(Dir[0]);CreateDIR(Dir[1]);CreateDIR(Dir[2])


Progress = ChargingBar('Reading and saving:', max=len(snaps))
for i,j in zip(root,snaps):
	time.sleep(random.uniform(0, 0.2))
	Progress.next()
	Read_Save(Dir,i,j)	
Progress.finish()
print('\n-> -------Reading completed.------- ')
