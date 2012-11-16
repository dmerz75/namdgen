#!/bin/bash
# rsync ggate

SOURCEDIR=/home/dale/Documents/valiant/workgen/namdgen/source100.da.c130/

#/home/dale/Documents/valiant/steele/01.da/100ss/100sa.da.c130/01.vac

DESTDIR=/mnt/hgfs/debian2shared/namd/

#scp -r $SOURCEDIR $DESTDIR
rsync -avh --include='*/' --include='*-npy.py' --include='*-expavg.py' --exclude='*' $SOURCEDIR $DESTDIR
