"""
Author: Antonel Ernest Pazargic
"""

connect("weblogic", "d41d8cd9", "t3://localhost:8001")

print('Setting up the JMS stuff...')

servermb=getMBean("Servers/AdminServer")

if servermb is None:

    print '@@@ No server MBean found'

else:
    edit()
    startEdit()

    print 'Creating File Store'
    cd('/')
    cmo.createFileStore('MyJMSFileStore')
    cd('/FileStores/MyJMSFileStore')
    cmo.setDirectory('MyJMSFileStore')
    set('Targets',jarray.array([ObjectName('com.bea:Name=AdminServer,Type=Server')], ObjectName))
    print 'The filestore has been successfully created.'

    print 'Creating JMS Server'
    cd('/')
    print 'Creating JMS Server.'
    cmo.createJMSServer('MyJMSServer')
    cd('/JMSServers/MyJMSServer')
    cmo.setPersistentStore(getMBean('/FileStores/MyJMSFileStore'))
    cmo.setTemporaryTemplateResource(None)
    cmo.setTemporaryTemplateName(None)
    cmo.addTarget(getMBean('/Servers/AdminServer'))

    print 'Creating JMS Module'
    cd('/')
    cmo.createJMSSystemResource('MyJmsSystemResource')
    cd('/JMSSystemResources/MyJmsSystemResource')
    cmo.addTarget(getMBean('/Servers/AdminServer'))
    cmo.createSubDeployment('MyJmsSubdeployment')

    print 'Creating Connection Factory'
    cd('/')
    cd('/JMSSystemResources/MyJmsSystemResource/JMSResource/MyJmsSystemResource')
    cmo.createConnectionFactory('MyJmsConnectionFactory')
    cd('/JMSSystemResources/MyJmsSystemResource/JMSResource/MyJmsSystemResource/ConnectionFactories/MyJmsConnectionFactory')
    cmo.setJNDIName('jms/MyJmsConnectionFactory')
    #set('SubDeploymentName','MyJmsSubdeployment')
    cd('/JMSSystemResources/MyJmsSystemResource/JMSResource/MyJmsSystemResource/ConnectionFactories/MyJmsConnectionFactory/SecurityParams/MyJmsConnectionFactory')
    cmo.setAttachJMSXUserId(false)
    cd('/JMSSystemResources/MyJmsSystemResource/JMSResource/MyJmsSystemResource/ConnectionFactories/MyJmsConnectionFactory/ClientParams/MyJmsConnectionFactory')
    cmo.setClientIdPolicy('Restricted')
    cmo.setSubscriptionSharingPolicy('Exclusive')
    cmo.setMessagesMaximum(10)
    #cd('/JMSSystemResources/MyJmsSystemResource/JMSResource/MyJmsSystemResource/ConnectionFactories/MyJmsConnectionFactory/TransactionParams/MyJmsConnectionFactory')
    #cmo.setXAConnectionFactoryEnabled(true)
    cd('/JMSSystemResources/MyJmsSystemResource/JMSResource/MyJmsSystemResource/ConnectionFactories/MyJmsConnectionFactory')
    cmo.setDefaultTargetingEnabled(true)

    print 'Creating Queue'
    cd('/')
    cd('/JMSSystemResources/MyJmsSystemResource/JMSResource/MyJmsSystemResource')
    cmo.createQueue('MyJmsQueue')
    cd('/JMSSystemResources/MyJmsSystemResource/JMSResource/MyJmsSystemResource/Queues/MyJmsQueue')
    set('JNDIName','jms/MyJmsQueue')
    set('SubDeploymentName','MyJmsSubdeployment')
    cd('/JMSSystemResources/MyJmsSystemResource/SubDeployments/MyJmsSubdeployment')
    cmo.addTarget(getMBean('/JMSServers/MyJMSServer'))

    print 'JMS Resources are Successfully Created'

    save()
    activate()

exit("y")
