#!/usr/bin/env python
import sys,os,time
import numpy as np

howmany= 10
t_data = np.array([])

def run_namd(i):
    st = time.time()
    os.system('namd2 +p1 smd.namd > run.log')
    tt = time.time()-st
    print tt
    os.system('mv da_smd_tcl.out %d-tef.dat' % i)
    os.system('python hb_rgyr.py %d' % i)
    return tt

for i in range(1,howmany+1):
    t1 = run_namd(i)
    t_data = np.append(t_data,t1)
    if i==1:
        os.system('mv da_smd.dcd %d-da_smd.dcd' % i)
    if i%4 == 0 or i%howmany == 0:
        np.save('%d_time' % i,t_data)
        np.savetxt('time.dat',t_data,fmt='%.4f')

os.system('rm *.BAK')
os.system('rm da_smd.coor')
os.system('rm da_smd.dcd')
os.system('rm da_smd.vel')
os.system('rm da_smd.xsc')
os.system('rm run.log')
