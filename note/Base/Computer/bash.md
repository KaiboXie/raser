
What is "shell"？

Linux:  sh, bash, tcsh 

#### shell
shell（壳），连接内核与用户的交互界面，通俗来说就是在Linux系统中发送命令的界面。

shell分为很多种类，常见的shell有sh，bash，csh，tcsh，常用的两种shell为tcsh和bash
程序中具体使用哪一种shell可以看第一行: #!/bin/bash 或者 #!/bin/bash。
其中#! 是说明文件类型的，"#!" 及后面的 "/bin/bash" 就表明该文件是一个 BASH 程序，需要由 /bin 目录下的 bash 程序来解释执行。
在Linux系统中使用 *echo $SHELL* 命令来查看当前shell


#### sh
sh的全称为Bourne shell，是由Bourne开发。
sh是UNIX上最标准的shell，很多UNIX版本都配有shell。
#### tcsh
tcsh是csh的增强版，完全兼容csh，csh是调用C shell，语法类似于C编程语言。
#### bash
bash shell是Linux中默认的shell，bash的命令语法大多来自ksh和csh。作为有个交互式shell，Tab键可以自动补全已经输入的程序名，文件名等等。


