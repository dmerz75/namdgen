#!/usr/bin/env python
import sys
import os

JOBID = os.environ['PBS_JOBID']
JOBID1 = JOBID.split('.')[0]

howmany= xxhowmanyxx

for i in range(1,howmany+1):
    os.system('namd2 +pxxnodecountxx smd.namd > run.log' % sys.argv[1])
    os.system('mv da_smd_tcl.out %d-tef.dat.%s' % (i,JOBID1))
    os.system('mv run.log %d-run.log.%s' % (i,JOBID1))
