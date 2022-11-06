# Git安装和使用

### 一、安装
安装指令：`sudo apt install git`

### 二、原理
本地仓库示意图：
![avatar](/版本库/git工作流程展示.png)   

分为两个区域：
    - 工作区：展示被管理的目录，即我们可以看见的部分。
    - 版本库：管理工作区的内容，即`.git`目录区域。
![avatar](/版本库/版本库.png)   

`.git`版本库划分为三个部分
    - 暂存区：工作目录提交`add`和检出`checkout <file>`的位置。
    - 目录树：git目录仓库，通过`commit`指令把暂存区文件的永久存放位置。
    - 对象库：每一次提交都会生成一个树对象结构，并存储到对象库里面

### 三、基本指令
1. 初始化仓库：`git init` *<font size=2>生成`.git`版本库</font>*
2. 添加到暂存库:`git add [文件匹配模式]` *<font size=2>生成数据对象</font>*
3. 添加到git仓库：`git commit [文件匹配模式]` 

### 四、过滤文件
1. 使用`touch .gitignore`创建文件
2. 在`.gitignore`里面增加需要排除的文件或目录
    - /out/ 为目录的表示方法，第一个`/`代表被控制的目录，`out/`代表目录。 

### 问题
1. 使用`git status`时，中文名称出现乱码
解决：`git config --global core.quotepath false`   core.quotepath为控制路径是否编码
