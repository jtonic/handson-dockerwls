#!/usr/bin/env bash

echo "Copying the files"
docker cp dockerfiles/12.2.1.1/container-scripts/connect.py wlsadmin:/u01/oracle/
docker cp dockerfiles/12.2.1.1/container-scripts/disconnect.py wlsadmin:/u01/oracle/
docker cp dockerfiles/12.2.1.1/container-scripts/change-password.py wlsadmin:/u01/oracle/
docker cp dockerfiles/12.2.1.1/container-scripts/read_password.py wlsadmin:/u01/oracle/

docker cp dockerfiles/12.2.1.1/container-scripts/change-password.sh wlsadmin:/u01/oracle/

docker cp password.secret wlsadmin:/u01/oracle/

echo "Making the sh file executable"
docker exec -it wlsadmin chmod a+x /u01/oracle/change-password.sh

echo "Executing the sh file"
docker exec -it wlsadmin /u01/oracle/change-password.sh
