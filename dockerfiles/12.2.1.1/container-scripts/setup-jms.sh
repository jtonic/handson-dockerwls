#!/usr/bin/env bash

# Author: Antonel Ernest Pazargic
echo "WL domain: " $DOMAIN_NAME
echo "WL admin port: " $ADMIN_PORT

# Setup the JMS
echo "Run the wlst script to setup the JMS"
wlst.sh -skipWLSModuleScanning /u01/oracle/setup-jms.py





