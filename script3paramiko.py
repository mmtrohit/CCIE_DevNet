from netmiko import ConnectHandler

cisco_device={"host":"10.1.1.10","port":22,"username":"cisco", "password":"cisco@123","device_type":"cisco_ios"}
connection=ConnectHandler(**cisco_device)
prompt=connection.find_prompt()
if ">" in prompt:
    connection.enable()

output=connection.send_command("show run")
print(output)

if not connection.check_config_mode():
    connection.config_mode()
    connection.send_command("username rohit secret cisco#123")

connection.send_command("username rohit secret cisco#123")

connection.exit_config_mode()
connection.send_command("show run | i user")
print(connection.find_prompt())

print("Closing the connection....")
connection.disconnect()


