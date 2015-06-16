#!/bin/bash

ANNOTATIONS=/home/vagrant/CHIC-services/annotations/annotation_service/
cd  $ANNOTATIONS

sudo python $ANNOTATIONS/rest_chic_annotation_8090.py 8090  2>&1 | tee log_8090.txt  &
sudo python $ANNOTATIONS/rest_chic_annotation_8091.py 8091  2>&1 | tee log_8091.txt  &

cd -
