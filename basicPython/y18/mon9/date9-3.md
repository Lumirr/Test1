1.https://www.kaggle.com/dejavu23/titanic-eda-to-ml-beginner   
2.代码比较工具使用;打断点，debug    
3.Dataframe的数据print输出显示为...省略号:https://blog.csdn.net/yagamil/article/
details/71642271     
  pd.set_option('display.max_columns', None)
4.one hot编码；python_pandas中的get_dummies使用https://blog.csdn.net/weixin_4238     
0251/article/details/80564652; enumerate()    
5.1 xvfb(虚拟屏幕)测试 
[服务器端]
sudo apt install xvfb x11vnc
Xvfb :screen-num -screen 0 1024x768x16 &
x11vnc -listen 0.0.0.0 -rfbport port -noipv6 -passwd passwd -display :screen-num
以上的红字请自行替换，如：
Xvfb :2 -screen 0 1024x768x16 &
x11vnc -listen 0.0.0.0 -rfbport 5900 -noipv6 -passwd zhijue -display :2
1024x768x16 是x，不是*
[用户端]
打开vncviewer连线即可，黑屏表示无东西显示，ssh连过去后运行export DISPLAY=:screen-num，随便开点GUI程序即可。
5.2 如何简化selenium crawler, 以下是一个思路，将selenium 的点击脚本自动转化为代码，https://github.com/corywalker/selenium-crawler   
6.Django,redis      
