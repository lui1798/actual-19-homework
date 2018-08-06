# actual-19-homework
# Reboot第19期实战班作业

## git提交千万不要用-f参数，-f 会干掉别人的代码，遇到报错可以问、
## git提交千万不要用-f参数，-f 会干掉别人的代码，遇到报错可以问、
## git提交千万不要用-f参数，-f 会干掉别人的代码，遇到报错可以问、

## 不要删除别人的代码！


## 目录结果

* lesson01：第一次作业提交的目录
    - woniu 用自己的名字新建文件间
        + zuoye.py 作业的代码文件
    - kk kk的目录
        + zuoye.py 作业代码文件


## 1.桌面软件添加代码（推荐初学者）


[详细说明](https://github.com/shengxinjing/my_blog/issues/4)



## 2.命令行添加代码

* [github 添加 ssh key](https://gist.github.com/yisibl/8019693)

```
第一次使用
git clone https://github.com/51reboot/actual-19-homework.git
cd actual-19-homework
mkdir woniu
echo  print 123 >> woniu/zuoye.py
git add .
git commit -m "first commit:joy:"
git push

后面添加代码，只需要下面几行即可
git pull # 在提交作业之前，记得一定要先git pull拉取仓库最新代码后，方可提交。
git add .
git commit -m "first commit"
git push 
```
## 3.Pycharm如何拉取和提交代码
配置git： 菜单settings-version control-git 填入git程序路径，点测试出版本号就成功。

拉代码：菜单：VCS-CHECKOUT FORM VERSION CTL 填入https://github.com/51reboot/actual-19-homework.git 拉取  linux有文件夹权限问题

提交代码：1.点git小对号 commit或 ctrl+k 提交到本地  2.点击菜单-vcs-git-push 提交到github

