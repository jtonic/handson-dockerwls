"""
Author: Antonel Ernest Pazargic
"""

connect("weblogic", "d41d8cd9", "t3://localhost:8001")
edit()
startEdit()

print('Setting up the JMS stuff...')

servermb=getMBean("Servers/AdminServer")
if servermb is None:
    print '@@@ No server MBean found'
else:

    print 'Creating File Store'

    cd('/')
    cmo.createFileStore('MyJMSFileStore')
    cd('/FileStores/MyJMSFileStore')
    cmo.setDirectory('MyJMSFileStore')
    set('Targets',jarray.array([ObjectName('com.bea:Name=AdminServer,Type=Server')], ObjectName))

    print 'The filestore has been successfully created.'



save()

exit("y")
