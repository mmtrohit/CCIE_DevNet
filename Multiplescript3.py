from netmiko import ConnectHandler

from def_function_paramiko import connect

cisco_device={"host":"10.1.1.10","port":22,"username":"cisco", "password":"cisco@123","device_type":"cisco_ios"}
connection=ConnectHandler(**cisco_device)
print("Enter the enable mode..")
connection.enable()
commands=["interface lo0","ip address 1.1.1.1 255.255.255.0","exit","username netmiko secret cisco"]
#1
#cmd = 'ip ssh version 2;access-list 1 permit any;ip domain-name network-automation.io'


## 2.
cmd = '''ip ssh version 2
#access-list 1 permit any
#ip domain-name net-auto.io
#'''

connection.send_config


# in enters automatically into global config mode and exists automatically at the end
print(connection.find_prompt())
connection.send_config_set(commands)
print(connection.find_prompt())
connection.send_command("wr")
print("Closing the connection...")
connection.disconnect()