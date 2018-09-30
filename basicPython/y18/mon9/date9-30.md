1.Postgresql查询时不区分大小写 https://www.cnblogs.com/my--blog-/p/5347989.html   
2.postgresql 性能优化https://www.cnblogs.com/churao/p/8494324.html   
3.postgresql语法：
  update yici_conf.brand_category_detail set modify_time = (select current_date)  select id, name, description from yici_conf.brand where description ~* '.*skyworth.*' order by id asc;
  postgresql数据库中删除重复字段？有合适的方法么——有   
4.正则贪婪非贪婪匹配https://www.cnblogs.com/xudong-bupt/p/3586889.html
5.delete from yici_conf.category_sub where (gp_segment_id, ctid) not in (select gp_segment_id, min(ctid) from yici_conf.category_sub group by cat_by_ec, gp_segment_id);表的去重研究一下;
id主键自增初始值修改:select setval('yici_conf.category_top_id_seq',(select max(id) from yici_conf.category_top) + 1 -- 注意序列名
update:update yici_conf.brand_category_detail set category_middle_id=xxx, category_top_name='文娱' where ...
delete去重:delete from yici_conf.brand_category_detail where id not in (select min(id) from yici_conf.brand_category_detail group by cat_by_ec, brand_id);
6.select * into yici_conf.brand_category_detail_tmp from yici_conf.brand_category_detail拷贝数据
7.时间戳转一般时间显示格式    
---
　timeStamp = 1381419600
  timeArray = time.localtime(timeStamp)
  otherStyleTime = time.strftime("%Y--%m--%d %H:%M:%S", timeArray)
   print(otherStyleTime)
---
8.postgresql数据库操作    
  select distinct sentiment_txt from data.dialogue_data;
