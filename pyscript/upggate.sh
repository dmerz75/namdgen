#!/bin/bash
# rsync ggate

SOURCEDIR=/home/dale/Documents/valiant/workgen/namdgen/
DESTDIR=dmerz3@ggate.chemistry.gatech.edu:/nethome/dmerz3/Documents/valiant/ggate/04.el/chi.el.c172/

#rsync -avh $SOURCEDIR $DESTDIR
scp -r $DESTDIR $SOURCEDIR
