"""
The WLST scripting for the deployment of an war in the WL.

Author: Antonel Ernest Pazargic
Date:
"""


def app_status(deploymentName, deploymentTarget):
    try:
        # domainRuntime()
        cd('domainRuntime:/AppRuntimeStateRuntime/AppRuntimeStateRuntime')
        currentState = cmo.getCurrentState(deploymentName, deploymentTarget)
        return currentState
    except:
        print 'Error in getting current status of ' + deploymentName + '\n'
        exit()


def deploy_start_app():
    print 'Deploying....'
    edit()
    startEdit()
    deploy('SimpleWar', '/u01/oracle/handson-wls-0.1-SNAPSHOT.war', targets='AdminServer')
    save()
    activate()
    # startApplication('SimpleWar')


def stop_undeploy_app():
    print 'Stopping and undeploying ....'
    stopApplication('SimpleWar')
    undeploy('SimpleWar')


if __name__ == '__main__' or __name__ == 'main':
    appName = 'SimpleWar'
    serverName = 'AdminServer'
    status = app_status(appName, serverName)
    print("The status of the application %s on server %s is %s" % (appName, serverName, status))
    if status is not None:
        stop_undeploy_app()
    deploy_start_app()
