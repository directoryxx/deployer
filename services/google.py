from google.cloud import compute_v1
from config import Config

class Google:

    def __init__(self):
        self.__instanceclient = compute_v1.InstancesClient()

    def get_instance_ip(self,tag):
        instance_list = self.__instanceclient.list(project=Config.PROJECT, zone=Config.ZONE)
        list_ip = []
        for instance in instance_list:
            if (',' in tag):
                fixTag = tag.split(",")
                for a in fixTag:
                    if (a in instance.name):
                        instance_get_request = self.__instanceclient.get(project=Config.PROJECT, zone=Config.ZONE, instance=instance.name)
                        list_ip.append(instance_get_request.network_interfaces[0].network_i_p)
            else:
                if (tag in instance.name):
                    instance_get_request = self.__instanceclient.get(project=Config.PROJECT, zone=Config.ZONE, instance=instance.name)
                    list_ip.append(instance_get_request.network_interfaces[0].network_i_p)

        return list_ip