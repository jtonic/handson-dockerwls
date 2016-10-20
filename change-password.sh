#!/usr/bin/env bash

docker cp dockerfiles/12.2.1.1/container-scripts/change-password.py wlsadmin:/u01/oracle/
docker cp dockerfiles/12.2.1.1/container-scripts/change-password.sh wlsadmin:/u01/oracle/

docker exec -it wlsadmin chmod a+x /u01/oracle/change-password.sh

docker exec -it wlsadmin /u01/oracle/change-password.sh
