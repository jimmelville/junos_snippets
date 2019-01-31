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


