# This program creates a telnet session using the
# pexpect library

import pexpect

# Add IP address, username, and password for your environment
ip_address = 'IP ADDRESS'
username = 'cisco'
password = 'cisco'

# Create Pexpect telnet session from pexpect library
session = pexpect.spawn('telnet ' + ip_address, timeout=20)

result = session.expect(['Username:', pexpect.TIMEOUT])

# Check for error, if so then print error and exit
if result != 0:
    print '--- FAILURE! creating session for: ', ip_address
    exit()

    # Session expecting username, enter it here
session.sendline(username)
result = session.expect(['Password:', pexpect.TIMEOUT])

# Check for error, if so then print error and exit
if result != 0:
    print '--- FAILURE! entering username: ', username
    exit()

# Session expecting password, enter it here
session.sendline(password)
result = session.expect(['>', pexpect.TIMEOUT])

# Check for error, if so then print error and exit
if result != 0:
    print ' FAILURE! entering password: ', password
    exit()

print '--- Success! connecting to: ', ip_address
print '---               Username: ', username
print '---               Password: ', password
print '------------------------------------------------------\n'
