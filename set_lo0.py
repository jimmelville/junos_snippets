from lab_devices import all_devices, test_devices, pe_devices
from jnpr.junos.utils.config import Config

import yaml

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
