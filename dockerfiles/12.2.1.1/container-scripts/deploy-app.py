"""
The WLST scripting for the deployment of an war in the WL.

Author: Antonel Ernest Pazargic
Date:
"""


def app_status(deploymentName, deploymentTarget):
    try:
        cd('domainRuntime:/AppRuntimeStateRuntime/AppRuntimeStateRuntime')
        currentState = cmo.getCurrentState(deploymentName, deploymentTarget)
        return currentState
    except:
        print 'Error in getting current status of ' + deploymentName + '\n'
        exit()


def deploy_start_app(deployment_name, deployment_target):
    print 'Deploying....'
    edit()
    startEdit()
    deploy(deployment_name, '/u01/oracle/handson-wls-0.1-SNAPSHOT.war', targets=deployment_target)
    save()
    activate()
    # startApplication('SimpleWar')


def stop_undeploy_app(deployment_name):
    print 'Stopping and undeploying ....'
    stopApplication(deployment_name)
    undeploy(deployment_name)


if __name__ == '__main__' or __name__ == 'main':
    app_name = 'handson-wls'
    server_name = 'AdminServer'
    status = app_status(app_name, server_name)
    print("The status of the application %s on server %s is %s" % (app_name, server_name, status))
    if status is not None:
        stop_undeploy_app(app_name, server_name)
    deploy_start_app(app_name, server_name)
