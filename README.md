# python3-ssh-rename-hostname
python 批量重命名主机脚本
# 使用
此处是在阿里云处直接导出的主机列表，只选机器名称和公网ip即可。
或者手动添加到列表中。然后直接运行即可。
脚本是使用密钥进行登录并带私钥密码，然后远程调用shell命令。
```
python3 set-hostname.py
```
