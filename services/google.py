from google.cloud import compute_v1
from config import Config

class Google:

    def __init__(self):
        self.__instanceclient = compute_v1.InstancesClient()

    def get_instance_ip(self,tag):
        instance_list = self.__instanceclient.list(project=Config.PROJECT, zone=Config.ZONE)
        list_ip = []
        for instance in instance_list:
            if (tag in instance.name):
                instance_get_request = self.__instanceclient.get(project=Config.PROJECT, zone=Config.ZONE, instance=instance.name)
                list_ip.append(instance_get_request.network_interfaces[0].network_i_p)
                # slack_data = {'text': "Trying Connect to : "+instance_get_request.name+" with IP : "+instance_get_request.network_interfaces[0].network_i_p}
                # response = requests.post(
                #     webhook_url, data=json.dumps(slack_data),
                #     headers={'Content-Type': 'application/json'}
                # )
                # ssh.connect(instance_get_request.network_interfaces[0].network_i_p, username='sisi',pkey=paramiko.RSAKey.from_private_key_file(cwd+'/id_rsa'))
                # stdin, stdout, stderr = ssh.exec_command('ls')
                # print(stdout.readlines())
                # ssh.close()

        return list_ip