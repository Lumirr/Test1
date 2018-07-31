1.PostgreSQL数据库使用。
2.
  1.先用python结合selenium生成关键词相关的html文件
  2.利用js结合神箭手爬虫api抓取数据库存到神箭手云中。
  3.编写python将云的数据放到自己的数据库中（data_process/graphql.py)。
  4.数据库中表client_zj_subcat4crawl增加字段。
  5.py编写爬取评论种子文件。如comment_seed.py.
  6.编写js。
3.psycopg2, re, 源码基础等。
4.__all__对外暴露的方法或变量，指(import *) 。
  __xxx是私有的，python内部做了重命名，不能被覆盖。
  _xxx表明此方法不是api，也是内部使用的。
  https://www.cnblogs.com/coder2012/p/4423356.html
