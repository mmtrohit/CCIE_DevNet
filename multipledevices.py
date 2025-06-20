from netmiko import ConnectHandler
with open("devices.txt","r") as f:
    output=f.read().splitlines()

new_device=list()

for ip in output:
    cisco_device = {
            'device_type': 'cisco_ios',
            'host': ip,
            'username': 'cisco',
            'password': 'cisco@123',
            'port': 22,
            'secret': 'cisco',  # this is the enable password
            'verbose': True
        }
    new_device.append(cisco_device)


for devices in new_device:
    connection=ConnectHandler(**devices)

    print("Enterring the enable mode:")
    connection.enable()

    file=input(f'Enter the file name(with proper directory){devices["host"]}')
    new_output=connection.send_config_from_file(file)
    print(new_output)

    print(f'Closing the connection for {devices["host"]} ')
    connection.disconnect()