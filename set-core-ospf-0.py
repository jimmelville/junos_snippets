from lab_devices import pe_devices, core_devices
from jnpr.junos.utils.config import Config

from utilities import get_dict_from_yaml

conf_file = "configs/junos-config-interfaces-ospf.conf"

core_to_core_dict = get_dict_from_yaml("configs/pe-core-mesh-interfaces.yaml")

for device in pe_devices+core_devices:
    core_to_core_interfaces = core_to_core_dict[device.hostname]

    config = {
        'interfaces': core_to_core_interfaces
    }

    dev = device.open()
    with Config(dev, mode='exclusive') as cu:
        cu.load(template_path=conf_file, template_vars=config, merge=True)
        cu.pdiff()
        cu.commit()
