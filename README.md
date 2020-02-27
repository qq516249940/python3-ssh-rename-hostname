# python3-ssh-rename-hostname
python 批量重命名主机脚本
# 使用
此处是在阿里云处直接导出的主机列表，只选机器名称和公网ip即可。
或者手动添加到列表中。然后直接运行即可。
脚本是使用密钥进行登录并带私钥密码，然后远程调用shell命令。
```
python3 set-hostname.py
```

问题:
UnicodeDecodeError: ‘utf-8’ codec can’t decode byte 0xd0 in position 0: invalid continuation byte



出现原因：文件不是 UTF8 编码的，而系统默认采用 UTF8 解码。解决方法是改为对应的解码方式。

解决办法：

找到csv文件–》右键–》打开方式–》记事本

打开记事本之后，选择头部菜单的“文件–》另存为”，可以看到文件的默认编码格式为ANSI,改为UTF-8即可。

