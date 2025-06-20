from netmiko import ConnectHandler

csr = {
    'device_type': 'cisco_ios',
    'host': '10.1.1.10',
    'username': 'cisco',
    'password': 'cisco@123'
}

device_list=[csr]
for device in device_list:
    with ConnectHandler(**device) as connection:
        print("Device connected successfully")
        output=connection.send_command("show ip int br")
        print(output)
