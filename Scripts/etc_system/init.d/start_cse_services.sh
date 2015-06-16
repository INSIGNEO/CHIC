#!/bin/bash

echo "Starting CSE services.."

CHIC_HOME=/home/vagrant

#Start taverna
su vagrant -c "bash -c '$CHIC_HOME/apache-tomcat-7.0.59/bin/startup.sh'"

#Start VPH-HF services
su vagrant -c "bash -c $CHIC_HOME/etc/start_vphhf_services.sh"

#Start CHIC services
su vagrant -c "bash -c $CHIC_HOME/etc/start_chic_services.sh"



