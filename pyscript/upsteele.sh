#!/bin/bash
# rsync ggate

SOURCEDIR=/home/dale/Documents/valiant/workgen/namdgen/source.da.c130/
DESTDIR=dmerz3@tg-steele.purdue.teragrid.org:/scratch/scratch96/d/dmerz3/valiant/steele/01.da/

#rsync -avh $SOURCEDIR $DESTDIR
scp -r $SOURCEDIR $DESTDIR
