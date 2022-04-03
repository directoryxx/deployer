import paramiko
from config import Config

class SSH:

    def connect(self,user,ip,command):
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        connect = ssh.connect(ip, username=Config.ROOTUSER,pkey=paramiko.RSAKey.from_private_key_file(Config.SSH_KEY))
        stdin, stdout, stderr = ssh.exec_command('sudo -u '+user+' sh -c "'+command+'"')
        ssh.close()
