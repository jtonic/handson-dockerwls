execfile("connect.py")

# =====================================
# Define the user password for weblogic
# =====================================
domain_name = os.environ.get("DOMAIN_NAME", "base_domain")
print "Domain name: %s" % domain_name

cd('/SecurityConfiguration/' + domain_name + '/Realms/myrealm/AuthenticationProviders/DefaultAuthenticator')
cmo.resetUserPassword('weblogic', 'jtonic123')

# cd('/Security/%s/User/weblogic' % domain_name)
# cmo.setPassword('jtonic')

execfile("disconnect.py")
