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
> git add .    // 保护本地所有更新 
> git stash  // 将代码保存到虚拟空间
> git remote update  // 更新远程最新代码至本地缓存（一个被隐藏的文件）
> git merge raser/main // 合并主站raser 最新代码（将上一行操作的缓存文件写进硬盘）
> git stash pop  // 将保存到虚拟空间的代码释放，检查是否与新代码有冲突
> git add . 
> git reset  // 选择不提交的文件。将文件路径黏贴在其后即可
> git commit -m ' Message'
> git push 



参考并做了修改： 
https://blog.csdn.net/qq_42764407/article/details/99678492
