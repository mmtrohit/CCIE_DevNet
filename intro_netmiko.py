from netmiko import Netmiko
from netmiko import ConnectHandler
csr = {
    'device_type': 'cisco_ios',
    'host':   '192.168.0.63',
    'username': 'admin',
    'password': 'admin'
}

connection=Netmiko(**csr)
print("connection done successfully..")
print(dir(connection))
show_output=connection.send_command("show run")

print(show_output)
print(connection.find_prompt())
print(connection.check_config_mode())
print(connection.check_enable_mode())
print(connection.config_mode())
print(connection.find_prompt())
print("Disconnection the connection..")
connection.disconnect()