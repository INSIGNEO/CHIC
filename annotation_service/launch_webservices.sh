#!/bin/bash

cd  /home/tartarini/PRODUCTION/annotation_service/

sudo python /home/tartarini/PRODUCTION/annotation_service/rest_chic_annotation.py 80  2>&1 | tee log_80.txt  &
sudo python /home/tartarini/PRODUCTION/annotation_service/rest_chic_annotation_8090.py 8090  2>&1 | tee log_8090.txt  &
sudo python /home/tartarini/PRODUCTION/annotation_service/rest_chic_annotation_8091.py 8091  2>&1 | tee log_8091.txt  &

cd -
