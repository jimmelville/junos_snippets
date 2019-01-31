from lab_devices import all_devices
from jnpr.junos.utils.config import Config

from utilities import get_dict_from_yaml

lo_interfaces = get_dict_from_yaml("configs/lo_interfaces.yaml")

for device in all_devices:
    config = "set interfaces lo0 unit 0 family inet address " + lo_interfaces[device.hostname] + "/24"
    dev = device.open()
    with Config(dev, mode='exclusive') as cu:
        cu.load(config, format='set', merge=True)
        cu.pdiff()
        cu.commit()
