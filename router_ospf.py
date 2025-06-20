import time

import paramiko
ssh_client=paramiko.SSHClient()
ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
router={"hostname":"10.1.1.10","port":"22","username":"cisco","password":"cisco@123"}
routers =[router]
for router in routers:
    print(f'Connecting to {router["hostname"]}')
    ssh_client.connect(**router, look_for_keys=False, allow_agent=False)
    shell=ssh_client.invoke_shell()
    shell.send("config t \n")
    shell.send("router ospf 1 \n")
    shell.send("net 0.0.0.0 0.0.0.0 area 0 \n")
    shell.send("end \n")
    shell.send("terminal lenght 0 \n")
    shell.send("show ip protocols \n")
    time.sleep(2)

    output=shell.recv(10000).decode()
    print(output)

    if ssh_client.get_transport().is_active()==True:
        print("closing connection")
        ssh_client.close()