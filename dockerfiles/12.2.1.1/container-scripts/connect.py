from read_password import read
print 'Connecting to admin server....'

passwd = read()
connect('weblogic', passwd, 't3://localhost:8001', adminServerName='AdminServer')

