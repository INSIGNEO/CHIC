#!/bin/bash

VPHHOME=/home/vagrant

#Initialize python environment.
source $VPHHOME/py2/bin/activate

python $VPHHOME/VPH-HF/web/sms_manage.py runserver localhost:8000 2>&1 | tee $VPHHOME/log/sms_8000 &
python $VPHHOME/VPH-HF/web/director_manage.py runserver localhost:8001 2>&1 | tee $VPHHOME/log/director_8001 &

