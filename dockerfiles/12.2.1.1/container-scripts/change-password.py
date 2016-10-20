from read_password import read

execfile("connect.py")

# =====================================
# Define the user password for weblogic
# =====================================
domain_name = os.environ.get("DOMAIN_NAME", "base_domain")
print "Domain name: %s" % domain_name

read()

print 'Changing the password'

cd('/SecurityConfiguration/' + domain_name + '/Realms/myrealm/AuthenticationProviders/DefaultAuthenticator')
cmo.resetUserPassword('weblogic', read())

print 'The password has been changed'


execfile("disconnect.py")
