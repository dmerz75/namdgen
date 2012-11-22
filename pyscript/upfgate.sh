#!/bin/bash
# rsync ggate

SOURCEDIR=/home/dale/Documents/valiant/workgen/namdgen/amb105b.da.c130/
DESTDIR=dmerz3@fgate-fs.chemistry.gatech.edu:/nethome/dmerz3/Documents/valiant/fgate/01.da/amb105b.da.c130/

rsync -avh $DESTDIR $SOURCEDIR
#rsync -avh $SOURCEDIR $DESTDIR
#scp -r $DESTDIR $SOURCEDIR
