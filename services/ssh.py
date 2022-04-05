from config import Config
import paramiko

class SSH:

    def __init__(self,ssh):
        self.ssh = ssh

    def connect(self,user,ip,command):
        self.ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        connect = self.ssh.connect(ip, username=Config.ROOTUSER,pkey=paramiko.RSAKey.from_private_key_file(Config.SSH_KEY))
        stdin, stdout, stderr = self.ssh.exec_command('sudo -u '+user+' sh -c "'+command+'"')
        return stderr.readlines()
