from logging import exception

from netmiko import ConnectHandler,exceptions
csr = {
    'device_type': 'cisco_ios',
    'host': '10.1.1.10',
    'username': 'cisco',
    'password': 'cisco@123'
}

device_list=[csr]
for device in device_list:
    try:
        print(f"\n{'#'*50} \n Connecting to device{device['host']}")
        connection=ConnectHandler(**device)
        print("Connection Done..")
        print(connection.find_prompt())
        print(connection.send_command("show ip int br"))
        connection.disconnect()

    except exceptions.NetMikoAuthenticationException as e:
        print(f"Error raised{e}",e)

    except exceptions.NetMikoTimeoutException as error:
        print("Error Raised", error)






