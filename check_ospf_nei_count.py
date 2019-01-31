from lab_devices import pe_devices, core_devices
from pprint import pprint
from jnpr.junos.utils.start_shell import StartShell


for device in pe_devices + core_devices:
    device.open()
    with StartShell(device, timeout=60) as ss:
        ospf_nei = ss.run('cli -c "show ospf neighbor"')
        print(device.hostname)
        pprint(ospf_nei)
        print()
    device.close()
