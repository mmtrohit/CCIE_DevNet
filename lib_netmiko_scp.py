import netmiko
import xmltodict
from pprint import pprint

"""from netmiko import ConnectHandler
from netmiko import file_transfer

device = {'device_type': 'cisco_ios',
           'host':"10.1.1.10",
           'username': 'cisco',
           'password': 'cisco@123',
           'port': 22,             # optional, default 22
           'secret': 'cisco',      # this is the enable password
           'verbose': True  }       # optional, default False


connection=ConnectHandler(**device)

transfer_output=file_transfer(connection,source_file="new_user.txt",dest_file="new_user.txt",file_system="flash0:", direction="put", overwrite_file=True)
print(transfer_output)
connection.disconnect() """



with open("py_to_xml.xml") as xml_in:
    new_inventory=xmltodict.parse(xml_in.read(), dict_constructor=dict)
    pprint(new_inventory)



