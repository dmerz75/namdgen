#!/usr/bin/env python
import sys
import os

JOBID = os.environ['PBS_JOBID']
JOBID1 = JOBID.split('.')[0]

howmany= xxhowmanyxx

for i in range(1,howmany+1):
    os.system('namd2 +idlepoll +isomalloc_sync +pxxnodecountxx +devices %s smd.namd > run.log' % sys.argv[1])
    os.system('mv da_smd_tcl.out %d-tef.dat.%s' % (i,JOBID1))

os.system('rm *.BAK')
os.system('rm *.coor')
os.system('rm *.dcd')
os.system('rm *.vel')
os.system('rm *.xsc')
os.system('rm run.log')
