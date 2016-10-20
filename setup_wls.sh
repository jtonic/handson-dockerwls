#!/usr/bin/env bash

mvn package -DskipTests

# Copying the files
echo 'Coping the files...'
docker cp dockerfiles/12.2.1.1/container-scripts/start-here.py wlsadmin:/u01/oracle/
docker cp dockerfiles/12.2.1.1/container-scripts/connect.py wlsadmin:/u01/oracle/
docker cp dockerfiles/12.2.1.1/container-scripts/setup-jms.py wlsadmin:/u01/oracle/
docker cp dockerfiles/12.2.1.1/container-scripts/deploy-app.py wlsadmin:/u01/oracle/
docker cp dockerfiles/12.2.1.1/container-scripts/disconnect.py wlsadmin:/u01/oracle/

docker cp dockerfiles/12.2.1.1/container-scripts/setup.sh wlsadmin:/u01/oracle/

docker cp target/handson-wls-0.1-SNAPSHOT.war wlsadmin:/u01/oracle


#making the sh executable
echo 'Making the script executable'
docker exec -it wlsadmin chmod a+x /u01/oracle/setup.sh

#running the script
echo 'Running the script'
docker exec -it wlsadmin /u01/oracle/setup.sh

echo 'DONE!!!'
