
## General Info 
[[史欣]]

We recommend team members to use VSCode for major programing tasks.  

<https://code.visualstudio.com>

Source code development at: <https://github.com/Microsoft/vscode>


### Remote X11 service configuration
[[杨涛]]

1. Install Remote - SSH and Remote X11 (SSH) in local Vscode
![image.png](https://raser-1314796952.cos.ap-beijing.myqcloud.com/media/20230112132545.png)
![image.png](https://raser-1314796952.cos.ap-beijing.myqcloud.com/media/20230112132627.png)

2.  Install Xming in local computer
[Xming X Server for Windows download | SourceForge.net](https://sourceforge.net/projects/xming/)

3. Configure X0.hosts:
Default path: C:\Program Files (x86)\Xming
(1).  Add the write permission for user: 右键文件属性->安全->编辑
![image.png](https://raser-1314796952.cos.ap-beijing.myqcloud.com/media/20230112133130.png)
(2) Insert the IP address of Remote Server:
The one of IP address of AFS: 202.122.33.195
![image.png](https://raser-1314796952.cos.ap-beijing.myqcloud.com/media/20230112133312.png)

Note: If you login the AFS account by lxslc7.ihep.ac.cn, the IP address will be random changed.

- 如果登录不同的服务器， 请把新的IP地址添加到上面的X0.hosts文件列表里面。 


4. Configure DISPLAY in Remote Server
Insert the line in ~/.bashrc:
'''
export DISPLAY={IP address of local computer}:0.0
'''

5. Restart local computer.

Mac OS 实现方法：
1. 下载XQuartz，在其中设置“允许从网络客户端连接”；
2. 配置vscode插件，同windows；
3. 在ssh配置文件中，为向服务器连接的字段添加ForwardX11 yes；
4. 连接服务器。如果失败，执行以下步骤然后重新登录。
	1. 从终端登入服务器，
	2. （如果是免密登陆）获取正式登陆身份
		1. 输入kinit，提示输入密码；
		2. 输入aklog -d 获取正式登陆身份
	3. 删除~/.Xauthority配置文件

如果成功：在服务器终端输入xclock，本地电脑会弹出一个窗口，里面有时钟图案

<<<<<<< HEAD:note/Base/Library/Computer/VSCode.md
免密登陆情形，如果仍然无法从vscode连接到服务器并成功执行xclock，可能是因为~/.Xauthority配置文件没有被正确的自动修改。解决办法正在探索中。
=======
免密登陆情形，如果仍然无法从vscode连接到服务器并成功执行xclock，可能是因为~/.Xauthority配置文件没有被正确的自动修改，可以参考以下步骤：
![](https://raser-1314796952.cos.ap-beijing.myqcloud.com/media/005808efcfccaf64ce04cdea15cb5a94.png)
>>>>>>> 695456d1c8e6837d9803abcd934847dd75b437fa:note/Base/Computer/VSCode.md

## VSCode in terminal 
[[史欣]]

<https://stackoverflow.com/questions/30065227/run-open-vscode-from-mac-terminal>

[Mac] Cmd+shift+p:   > Shell Command: Install code in PATH 


## PDF Plugin 
[[杨涛]]

To preview pdf file, install extension vscode-pdf in Vscode. 

Then open the pdf with code (or rcode) from terminal. 

## File EOL 

Solution  : /usr/bin/env: ‘python\r’: No such file or directory

VScode for Chinese version：
文件->首选项->设置->文件
Change ''file.eol'' : ''\r\n'' -> ''file.eol'' : ''\n''


[1]: https://ernie.io/2011/12/12/textmate-2-rmate-awesome/

