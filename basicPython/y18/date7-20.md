1.Ubuntu安装Anaconda
  - 官网下载对应版本
  - 打开terminal,输入如下命令,然后回车 
  - bash /home/tingting/Downloads/Anaconda2-4.0.0-Linux-x86_64.sh 
  - 这里的/home/tingting/Downloads/是存放Anaconda2-4.0.0-Linux-x86_64.sh的路径
  - 打开新的terminal,输入Jupyter notebook,发现jupyter被成功安装了    
2.Ubuntu修改环境变量
  - 修改profile文件：
  - #vi /etc/profile
  - 在里面加入:
  - export PATH="$PATH:/opt/au1200_rm/build_tools/bin"
  - 用export修改环境变量：
  - https://blog.csdn.net/u013176681/article/details/38662985      
3.conda安装Tensorflow
  -【深度学习】Ubuntu16.04+Anaconda安装+换源+环境创建+tensorflow安装
  - https://blog.csdn.net/luojie140/article/details/78696330      
4.markdown末尾多敲几个空格可换行（？）    
5.
  1.当我修改了/etc/profile文件，我想让它立刻生效，而不用重新登录；这时就想到用source命>令，如:source /etc/profile。
2.Tensorflow
  1.Tensorflow中文教程：http://www.tensorfly.cn/tfdoc/get_started/os_setup.html。
  2.可开启GPU支持（应该是显卡什么的）。
3.学习一门语言可在github上找些练习做。
4.'ctrl+shift+t'在当前终端新建一个窗口。
5.git使用：
  1.进入项目文件夹：git status;git add (-a) xxx;git commit -m'xxx';git push origin master;
  2.git pull origin master
6.tar -xzvf xxx.tar.gz -C xxx,-C指定解压到目录。
7.Ubuntu 16.04安装IntelliJ出品的数据库管理工具DataGrip:
  https://www.cnblogs.com/EasonJim/p/7868645.html
8.神箭手云相关。pip install shenjian
9.PostgreSQL数据库。
10.datagrip登录云数据库;连数据。
11.pip安装的包conda能看到（我的版本）。
12.git reset HEAD 如果后面什么都不跟的话 就是上一次add 里面的全部撤销了
git reset HEAD XXX/XXX/XXX.java 就是对某个文件进行撤销了
13.conda虚拟环境的基本使用：https://www.aliyun.com/jiaocheng/516008.html
14.Ubuntu16.04基于Anaconda安装Tensorflow:https://www.cnblogs.com/tiansheng/p/7281290.html
15.source deactivate flappbird:关闭conda打开的虚拟环境。
16.conda info xxx查看某包的依赖。
17.anaconda-navigator:打开导航窗口。
18.top查看物理内存等使用情况。https://www.cnblogs.com/shihaiming/p/5949272.html。
19.linux安装nvidia驱动与tensorflow。https://blog.csdn.net/hejunqing14/article/details/73194795。


