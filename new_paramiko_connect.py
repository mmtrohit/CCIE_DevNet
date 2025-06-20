import time
import paramiko

ssh_client=paramiko.SSHClient() ## Creating SSH client object
ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
router={"hostname":"10.1.1.10","port":"22","username":"cisco","password":"cisco@123"}
print(f'Connecting to {router["hostname"]}')
ssh_client.connect(**router, look_for_keys= False, allow_agent=False)
#ssh_client.connect(hostname="10.1.1.10", port=22, username="cisco", password="cisco@123", look_for_keys=False, allow_agent=False)
shell=ssh_client.invoke_shell()
shell.send("terminal lenght 0 \n")
shell.send("show veriosn \n")
shell.send("show ip int brief \n")
time.sleep(1)

## Reading the lines from output

output=shell.recv(10000).decode()
print(output)



if print(ssh_client.get_transport().is_active())== True :
    print("Closing Connection")
    ssh_client.close()







