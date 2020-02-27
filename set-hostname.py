# -*- coding: utf-8 -*-
# author: chunk
# date: 2020-02-26
import csv
import paramiko


def ssh_client(ip,hostname):
    key = paramiko.RSAKey.from_private_key_file("xxx/id_rsa" , password="xxxxx")
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    print("connecting")
    ssh.connect( hostname = ip, username = "root", pkey = key)
    print("connected")
    command = "hostnamectl set-hostname " + hostname
    stdin, stdout, stderr = ssh.exec_command(command)

    for i in stdout.readlines():
        print(i)
    ssh.close()  



with open('stocks2.csv') as f:
    f_csv = csv.reader(f)
    headers = next(f_csv)
    print(headers)
    for row in f_csv:
        # print(row)
        print("------------------")
        print(row[0])
        print(row[1])
        ssh_client(row[1],row[0])






