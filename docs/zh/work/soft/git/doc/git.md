# 
另一个分支的所有代码变动
git merge  
只需要部分代码变动（某几个提交）
git cherry-pick




# 查看远程分支

git branch -r

# 创建并切换分支
这个命令是将git branch newbranch和git checkout newbranch合在一起的结果。

git checkout -b localbranchName remoteBranchname

# 刷新远程分支

git remote update



# 忽略已经push的文件

git rm -r --cached */target/*

git commit -m '忽略文件'

# clone 非22 端口

> git clone ssh://git@gitee.com:22/wjn0918/linkis.git
