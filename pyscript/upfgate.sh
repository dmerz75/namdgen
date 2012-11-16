#!/bin/bash
# rsync ggate

SOURCEDIR=/home/dale/Documents/valiant/workgen/namdgen/asmd100ppn4/
DESTDIR=dmerz3@fgate.chemistry.gatech.edu:/nethome/dmerz3/Documents/valiant/fgate/01.da/

#rsync -avh $SOURCEDIR $DESTDIR
scp -r $SOURCEDIR $DESTDIR
