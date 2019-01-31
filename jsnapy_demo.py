from jnpr.junos import Device
from jnpr.junos.utils.config import Config

from pprint import pprint
import yaml

user = "root"
passwd = "root123"

p1 = Device(host="p1", user=user, passwd=passwd, port="22")
p2 = Device(host="p2", user=user, passwd=passwd, port="22")
p3 = Device(host="p3", user=user, passwd=passwd, port="22")
p4 = Device(host="p4", user=user, passwd=passwd, port="22")
p5 = Device(host="p5", user=user, passwd=passwd, port="22")
p6 = Device(host="p6", user=user, passwd=passwd, port="22")

pe1 = Device(host="pe1", user=user, passwd=passwd, port="22")
pe2 = Device(host="pe2", user=user, passwd=passwd, port="22")

test_devices = [p1]
core_devices = [p2, p3, p4, p5, p6]
pe_devices = [pe1, pe2]
all_devices = test_devices+core_devices+pe_devices


def get_dict_from_yaml(yaml_filepath):
    with open(yaml_filepath, 'r') as stream:
        try:
            return yaml.load(stream)
        except yaml.YAMLError as e:
            print(e)


lo_interfaces = get_dict_from_yaml("configs/lo_interfaces.yaml")

for device in all_devices:
    config = "set interfaces lo0 unit 0 family inet address " + lo_interfaces[device.hostname] + "/24"
    print(config)
    dev = device.open()
    with Config(dev, mode='exclusive') as cu:
        cu.load(config, format='set', merge=True)
        cu.pdiff()
        cu.commit()


# core_devices_interfaces= {
#     'interfaces': ['ge-0/0/1', 'ge-0/0/2', 'ge-0/0/3'],
#     'description': 'MPLS interface',
#     'family': 'mpls'
# }
# pe_devices_interfaces= {
#     'interfaces': ['ge-0/0/1', 'ge-0/0/2'],
#     'description': 'MPLS interface',
#     'family': 'mpls'
# }
#