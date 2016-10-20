def read():
    f = open('/u01/oracle/password.secret', 'r')
    passwd = f.read().strip()
    f.close()
    print("The password: '%s'" % passwd)
    return passwd
