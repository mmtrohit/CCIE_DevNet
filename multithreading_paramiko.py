import threading

import paramiko
import time

def backup(router):
#   router1 = {"server_ip":'10.1.1.10', 'server_port': 22, 'user': 'u1', 'passwd': 'cisco'}
    ssh_client=paramiko.SSHClient()
    ssh_client.connect(**router)
    shell=ssh_client.invoke_shell()
    shell.send("terminal lenght 0 \n")
    shell.send("show run \n")
    time.sleep(2)

    output=shell.recv(10000).decode()
    output_list=output.splitlines()
    output_list=output_list[11:-1]
    new_output="/n".join(output_list)

    from datetime import datetime
    now=datetime.now()
    year=now.year
    month=now.month
    day=now.day

    file_name=(f'router{["hostname"]}_{year}_{month}_{day}.txt')
    with open(file_name,"w") as f:
        f.write(new_output)


router1={"hostname":"10.1.1.10","port":"22","username":"cisco","password":"cisco@123"}
backup(router1)


th=threading.Thread(target=backup, args=(router1,))
th.start()
th.join()