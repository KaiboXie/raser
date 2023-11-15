# Git Usage 


# 安装

## Windows

https://git-scm.com/download/win


## Set the username and e-mail address 

    $ git config --global user.name "Firstname Lastname"
    $ git config --global user.email "your_email@example.com"
    $ git config --global color.ui auto

## Register github account on github.com

 - Create SSH key:

    $ ssh-keygen -t rsa -C "your_email@example.com"
    Generating public/private rsa key pair.
    Enter file in which to save the key
    (/Users/your_user_directory/.ssh/id_rsa):
    Enter passphrase (empty for no passphrase):
    Enter same passphrase again:
    Enter $ cat ~/.ssh/id_rsa.pub and copy the SSH key

Github.com -> Settings -> SSH and GPG keys -> New SSH keys, then paste the key

    $ ssh -T git@github.com

Clone jadepix to your computer: 

    $ git clone git@github.com:cepc/jadepix.git

Make what you forked synchronize with the original one [1]:

    git remote add upstream git@github.com:cepc/jadepix.git
    git fetch upstream
    git merge upstream/master
    git push origin master

[1]: http://blog.csdn.net/myuantao3286286/article/details/50477139


## git 命令提交步骤 on raser

> git status  // 查看修改过的文件
> git stash  // 将自己更改过的代码暂时保存到虚拟空间
> git remote update  // 更新远程最新代码至本地缓存（一个被隐藏的文件夹'.git'）
> git merge raser/main  // 合并主站raser 最新代码（将上一行操作的缓存文件写进硬盘）
> git stash pop  // 将保存到虚拟空间的代码释放，检查是否与新代码有冲突
> git reset  // 选择不提交的文件。将文件路径黏贴在其后即可
> git commit -m ' Message'
> git push 


---
# git常见操作流程

[[李星臣]]
1. 一系列初始操作（仅在创建时使用）
	- 建立本地git仓库
		- git clone https://code.ihep.ac.cn/1902370441/raser.git （自己远程仓库的HTTPS）
	- 与组里的git仓库建立连接
		- git remote add raser https://code.ihep.ac.cn/raser/raser.git （组远程仓库的HTTPS）
	- 配置账号和邮箱信息
		- git config user.name "your-username"
		- git config user.email "your-email-address"
2. 从组里拉取最新代码操作
	- git remote update
	- git merge raser/main
	- 若上一步报错有冲突
		- git add .
		- git stash
		- git merge raser/main
		- git stash pop
3. 将自己更新的代码推到组的服务器上
	- 点击你想更新的文件的加号，他就会从changes到staged changes里，然后在上面的框里给你更改的文件写上备注，最后再点击commit              ![git-operate-1.png|300](https://raser-1314796952.cos.ap-beijing.myqcloud.com/media/git-operate-1.png)
	- git remote update
	- git merge raser/main (确保你更新了组里的最新版本)
	- git push
	- 打开你的远程git库，点击merge request，创建new merge request![git-operate-2.png](https://raser-1314796952.cos.ap-beijing.myqcloud.com/media/git-operate-2.png)

---
# 常见报错与解答

- ![git-error-2023-1-14.png|400](https://raser-1314796952.cos.ap-beijing.myqcloud.com/media/git-error-2023-1-14.png) [[李星臣]]
	- 需要在commit上面的窗口写一信息，该栏不能是空的![git-solve-2023-1-14.png](https://raser-1314796952.cos.ap-beijing.myqcloud.com/media/git-solve-2023-1-14.png)
- 创建文件之后才想到要ignore [[符晨曦]]
	- git -rm --cached 想ignore的文件
	- commit


## Git Large File Storage 

https://git-lfs.com

1. Install git lfs in your system ：$ git lfs install
2. Pull the large files from remote : $ git lfs pull 


## Git Add others repository

$ git remote add shixin https://code.ihep.ac.cn/shixin/raser.git 
$ git remote update 
$ git merge shixin/main

