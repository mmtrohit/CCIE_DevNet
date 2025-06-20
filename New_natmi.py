from netmiko import  ConnectHandler

router1= {host="10.1.1.10",port=22,username="cisco",password="cisco@123", device_type="cisco_ios"}
connection =ConnectHandler(**router)
prompt=connection.find_prompt()
print(prompt)
connection.enable()
output= connection.send_command("show ip int br")
print(output)
print("disconnecting the connection")
connection.disconnect()