#######################
from Packages import *
#######################

def f_fl(L,padding):
	return(float(L)-2.*padding)

def f_lunit(box,Mpc,fl):
	return(box*Mpc/fl)


def f_vunit(h0t0,H0,h100,box,Mpc,fl,yr):

	lunit=f_lunit(box,Mpc,fl)
	tunit=h0t0/H0/h100

	return(lunit/tunit)


def f_convV(h0t0,H0,h100,box,Mpc,yr,atime,L,padding):
	fl=f_fl(L,padding)
	vunit=f_vunit(h0t0,H0,h100,box,Mpc,fl,yr)

	return(vunit*fl*atime/100000.)

def f_convL(box,Mpc,atime,L,padding):

	fl=f_fl(L,padding)
	lunit=f_lunit(box,Mpc,fl)

	return(lunit*fl*atime/Mpc) 