#!/usr/bin/env python
import os, os.path
from glob import glob
import numpy as np
from random import randint

my_dir=os.path.abspath(os.path.dirname(__file__))
acc=[]

#os.chdir(os.path.join(my_dir,opdir))
num='xxnumxx'
dnum='xxnumxx.data'
ddir=os.path.join(my_dir,dnum)
if not os.path.exists(ddir):
    os.makedirs(ddir)

def pack(i):
    acc=[]
    for path in glob(os.path.join(my_dir,'%s.*/*-tef.dat*' % num)):
        if len(acc)==25:
	    break
        print path
        idn=randint(10000,99999)
        sample_i = np.loadtxt(path)
        os.remove(path)
        acc.append(sample_i)
    os.chdir(ddir)
    data = np.array(acc)
    np.save('%s_%d_%s' % (num,i,idn),data)

count=0
for path in glob(os.path.join(my_dir,'%s.*/*-tef.dat*' % num)):
    count+=1
print count
for i in range(1,(count/20)+2):
    pack(i)
