#!/usr/bin/env python
import os, os.path
from glob import glob
import numpy as np
from random import randint
import datetime

my_dir=os.path.abspath(os.path.dirname(__file__))
acc=[]

for path in glob(os.path.join(my_dir,'01.*/10_time.npy')):
    print path
    sample_i = np.load(path)
    print sample_i.shape
    acc.append(sample_i)
data=np.concatenate(acc,axis=0)

datam=data.mean()

print data
print datam

'''
# PLOT - pmf
fig=plt.figure()
plt.clf()

for index in plot_indices:
   e_i = data[index,::,1]
   w_i = work[index,::]
   plt.plot(domain[::1],w_i[::1],'k-',linewidth=0.4)

plt.plot(domain[::1], deltaf[::1],'r-',linewidth=5)
plt.plot(domain[::1], deltaf[::1],'k--',linewidth=0.6)

plt.xlabel('Extension (A)')
plt.ylabel('Work (kcal/mol)')
plt.title('NAMD - SMD - rda\n'+str(data.shape[0])+'trj vac -1000.0 A/ns')

#plt.ylim([ymin,ymax])
plt.xlim([xmin-.1,xmax+.1])

plt.draw()
fig.savefig('time.png')
fig.savefig('time.eps')
'''
