
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

