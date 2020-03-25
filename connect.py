import paramiko as s
ssh = s.SSHClient()
ssh.set_missing_host_key_policy(s.AutoAddPolicy())
ssh.connect(hostname="192.168.2.5", username="derrick", password="Ed921213-")
ssh_stdin, ssh_stdout, ssh_stderr = ssh.exec_command('ls')
print()
print( '\n'.join( ssh_stdout.readlines()))
print()