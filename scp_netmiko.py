from netmiko import ConnectHandler, file_transfer

#from netmiko import Netmiko

csr = {
    'device_type': 'cisco_ios',
    'host': '192.168.0.63',
    'username': 'admin',
    'password': 'admin'
}

connection=ConnectHandler(**csr)
transfer=file_transfer(connection,source_file="show_run.txt",dest_file="show_run.txt",file_system="disk0:", overwrite_file= True, direction="put")
print("file trasnferred successfully")
print(transfer)
connection.disconnect()