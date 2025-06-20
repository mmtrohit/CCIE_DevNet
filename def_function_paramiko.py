import time
import paramiko

def connect(server_ip,hostname,pswd, server_port):
    ssh_client=paramiko.SSHClient()
    ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    print(f"connecting to {server_ip}")
    ssh_client.connect(hostname=server_ip,port=server_port,username=hostname,password=pswd)
    return ssh_client

def get_shell(ssh_client):
    shell=ssh_client.invoke_shell()
    return shell

def send_command(shell,command,timeout=1):
    shell.send("terminal lenght 0 \n")
    shell.send("terminal lenght 0 \n")
    shell.send("show veriosn \n")
    shell.send("show ip int brief \n")
    time.sleep(1)


def show(shell,n=10000):
    output=shell.recv(n).decode()
    return  output

def close(ssh_client):
    if ssh_client.get_transport().is_active() == True:
        print("Closing the connection..")
        ssh_client.close()



############Calling the function ###############

if __name__== "__main__":
    router1 = {'server_ip': '10.1.1.10', 'server_port': '22', 'hostname': 'cisco', 'pswd': 'cisco@123'}
    client=connect(**router1)

    shell=get_shell(client)

    send_command(shell, 'term len 0')
    send_command(shell, 'sh version')
    send_command(shell, 'sh ip int brief')

    output=show(shell)
    print(output)





