from netmiko import ConnectHandler
import logging


csr = {
    'device_type': 'cisco_ios',
    'host':   '10.1.1.10',
    'username': 'cisco',
    'password': 'cisco@123'
}

connection=ConnectHandler(**csr)
print("connection done successfully..")

import logging
logging.basicConfig(filename="demo_netmiko.log", level=logging.DEBUG)
logger=logging.getLogger("netmiko")
logger.info("Connected")