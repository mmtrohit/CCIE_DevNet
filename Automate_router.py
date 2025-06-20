import def_function_paramiko
client=def_function_paramiko.connect("10.1.1.10","cisco","cisco@123",22)
shell=def_function_paramiko.get_shell(client)
def_function_paramiko.send_command(shell,"terminal length 0")
def_function_paramiko.send_command(shell,"show ip int br")
output = def_function_paramiko.show(shell)
print(output)


