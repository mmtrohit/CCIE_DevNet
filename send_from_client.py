import paramiko
import time

from router_ospf import ssh_client


def connect(server_ip,server_port,user,pswd):
    ssh_client=paramiko.SSHClient()
    ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    print(f"connecting to {server_ip}")
    ssh_client.connect(hostname=server_ip,port=server_port,username=user,password=pswd)
    return ssh_client

def get_shell(ssh_client):
    shell=ssh_client.invoke_shell()
    return shell

def send_cmd(shell,cmd,t=1):
    shell.send(cmd + "\n")
    shell.send(cmd + "\n")
    shell.send(cmd+ "\n")
    time.sleep(t)

def show(shell,n):
    shell.recv(10000)
    return shell.recv(10000).decode()


def check(ssh_client):
    if ssh_client.get_transport().is_active() == True:
        print("Closing the connection..")
        ssh_client.close()



if __name__=="__main__":
    router1 = {'server_ip': '10.1.1.10', 'server_port': '22', 'hostname': 'cisco', 'pswd': 'cisco@123'}
    client = connect(**router1)

    shell=get_shell(ssh_client)
    send_cmd(shell,"show ip int br")
    output=show(shell,10000)
    print(output)
    check(client)
