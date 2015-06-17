#!/bin/bash

VPHHOME=/home/vagrant

#Initialize python environment.
source $VPHHOME/py2/bin/activate

python2 $VPHHOME/VPH-HF/web/sms_manage.py migrate
python2 $VPHHOME/VPH-HF/web/sms_manage.py runserver 0.0.0.0:8000 2>&1 | tee $VPHHOME/log/sms_8000 &

python2 $VPHHOME/VPH-HF/web/director_manage.py migrate
python2 $VPHHOME/VPH-HF/web/director_manage.py runserver 0.0.0.0:8001 2>&1 | tee $VPHHOME/log/director_8001 &

