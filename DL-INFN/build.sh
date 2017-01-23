#!/usr/bin/env bash

OUT_DIR=dlworkshop

rm -rf $OUT_DIR

rsync -aP --exclude=.* ./* ./$OUT_DIR/

if [ "$1" != "solutions" ]; then
    # echo 'dude'
    rm -rf ./$OUT_DIR/solutions ./$OUT_DIR/extras/solutions
    rm ./$OUT_DIR/build.sh
    rm ./$OUT_DIR/topics.md
fi

NOW=$(date +"%m-%d-%Y")
DEPLOYDIR=~/Documents/Dropbox/DataWeekendsDeployments/DLWorkshop-$NOW
mkdir -p ~/Documents/Dropbox/DataWeekendsDeployments/
mkdir $DEPLOYDIR

cp -r $OUT_DIR/* $DEPLOYDIR
cd ..
rm -rf $OUT_DIR