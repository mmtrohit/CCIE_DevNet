from netmiko import ConnectHandler
csr = {
    'device_type': 'cisco_ios',
    'host': '192.168.0.63',
    'username': 'admin',
    'password': 'admin'
}
connection=ConnectHandler(**csr)
cmd1= "copy run start-up"
cmd2= r"Destination filename"
cmd5=[[cmd1,cmd2],["\n","Do you want to over write"],["\n"]]
# output=connection.send_multiline([cmd1,cmd2],["\n", "Do you want to over write"])
#cmd_output=connection.send_multiline(cmd5)
connection.config_mode()
cmd_output=connection.send_config_set(cmd5)
print(cmd_output)