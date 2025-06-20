import paramiko
import getpass
ssh_client=paramiko.SSHClient()
ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
pswd=getpass.getpass("Enter the password : ")
router={"hostname":"10.1.1.10","port":"22","username":"cisco","password":pswd}
ssh_client.connect(**router,look_for_keys=False,allow_agent=False)
shell=ssh_client.invoke_shell()
shell.send(" terminal length 0")
shell.send("show run")
output=shell.recv(1000).decode()

with open("show_run.txt","w") as f:
    f.write(output)