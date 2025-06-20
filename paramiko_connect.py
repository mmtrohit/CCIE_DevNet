import time
#from encodings.uu_codec import uu_decode

import paramiko
#import getpass

#password=getpass.getpass("Enter the password")
ssh_client=paramiko.SSHClient()
print(type(ssh_client))
print("Connecting to 10.1.1.10")
ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh_client.connect(hostname="10.1.1.10", port =22, username="cisco", password="cisco@123", look_for_keys= False, allow_agent=False)

router={"hostname": "10.1.1.10", "port":"22","username":"u1","password":password}
ssh_client.connect(**router, look_for_keys=False, allow_agent=False)

shell= ssh_client.invoke_shell()

shell.send("config t \n")
shell.send("router ospf 1 \n")
shell.send("net 0.0.0.0 0.0.0.0 are 0 \n")
shell.send("end \n")
shell.send("terminal length 0 \n")
shell.send("show ip protocols \n")
shell.send("show version \n")
shell.send("terminal length 0 \n")
time.sleep(1)
output=shell.recv(10000)
print(type(output))
output=output.decode("utf-8")

if ssh_client.get_transport().is_active() == True:
    print("Closing Connection")
    ssh_client.close()