#!/bin/bash
TEMPDIR=/tmp/dataweekends
rm -rf $TEMPDIR
mkdir $TEMPDIR
cp -r * $TEMPDIR
cd $TEMPDIR
find . -type d -name "*git*" | xargs rm -rf
find . -type f -name "*solution*" | xargs rm -rf
rm deploy.sh

cd finalproject/ml
rm -rf wikidata
rm -rf my_model.dill.gz

NOW=$(date +"%m-%d-%Y")
DEPLOYDIR=~/Documents/Dropbox/DataWeekendsDeployments/MLWorkshop-$NOW
mkdir -p ~/Documents/Dropbox/DataWeekendsDeployments/
mkdir $DEPLOYDIR

cp -r $TEMPDIR/* $DEPLOYDIR
cd ..
rm -rf $TEMPDIR