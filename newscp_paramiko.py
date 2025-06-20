import paramiko
from scp import SCPClient

ssh_client=paramiko.SSHClient()
print(type(ssh_client))
print("Connecting to 10.1.1.10")
ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh_client.connect(hostname="10.1.1.10", port =22, username="cisco", password="cisco@123", look_for_keys= False, allow_agent=False)

scp=SCPClient(ssh_client.get_transport())
scp.put("devices.txt","/flash0") ### to copy file
scp.put("direcory1", recursive=True, remote_path="flash0") ### to copy directory
scp.get()## to copy from device
scp.close()