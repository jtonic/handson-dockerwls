###Steps to run a wlst script


##### Manual
* copy the wlst py and sh scripts

        $ docker cp dockerfiles/12.2.1.1/container-scripts/setup-jms.py wlsadmin:/u01/oracle/
        $ docker cp dockerfiles/12.2.1.1/container-scripts/setup-jms.sh wlsadmin:/u01/oracle/


* setup execution permission for scripts

        $ docker exec -it wlsadmin chmod a+x /u01/oracle/setup-jms.sh
        $ docker exec -it wlsadmin chmod a+x /u01/oracle/setup-jms.py

* run script

        $ docker exec -it wlsadmin /u01/oracle/setup-jms.sh
        

##### More information about setting up the JMS through WLST at:

        http://www.albinsblog.com/2013/03/set-up-jms-resources-through-wlst-script.html#.WAecoZh976o
    






    