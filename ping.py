import os
def ping (hostname):
    response = os.system('ping -n 1 %s'%hostname)
    if response == 0:
        print (hostname, 'is up!')
    else:
        print (hostname, 'is down!')