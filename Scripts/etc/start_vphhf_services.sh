#!/bin/bash

VPHHF=/home/vagrant/VPH-HF/web

#Initialize python environment.
source $HOME/py2/bin/activate

python2 $VPHHF/sms_manage.py migrate
python2 $VPHHF/sms_manage.py runserver 0.0.0.0:8000 2>&1 | tee $HOME/log/sms_8000 &

python2 $VPHHF/director_manage.py migrate
python2 $VPHHF/director_manage.py runserver 0.0.0.0:8001 2>&1 | tee $HOME/log/director_8001 &

python2 $VPHHF/chic_insilicotrial_mockup/manage.py migrate
python2 $VPHHF/chic_insilicotrial_mockup/manage.py runserver 0.0.0.0:8002 2>&1 | tee $HOME/log/insilico_8002 &

