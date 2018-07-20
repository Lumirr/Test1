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

