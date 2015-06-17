#!/bin/bash

CHICSERVICES=$HOME/CHIC-services

#Need to use the python from the system.
# initializing python environment
source $HOME/py2/bin/activate

echo "Launch CHIC annotation web services"
cd $CHICSERVICES/annotations/annotation_service/
python2 rest_chic_annotation_8090.py 8090 2>&1 | tee $HOME/log/annotation_8090  &
python2 rest_chic_annotation_8091.py 8091 2>&1 | tee $HOME/log/annotation_8091  &
cd -

# initializing python environment
source $HOME/py3/bin/activate
python3 $CHICSERVICES/repositories/repository/manage.py migrate
python3 $CHICSERVICES/repositories/repository/manage.py runserver 0.0.0.0:8010 2>&1 | tee $HOME/log/model_and_datarepo_8010 &
