# maoyan
获取猫眼电影按评价排行的前300部电影的所有评论
## 项目介绍
此爬虫是基于Scrapy框架的猫眼电影爬虫，可以获取猫眼电影排行前300的所有评论、用户评分、用户位置等信息
## 抓取思路
使用Charles对猫眼电影手机客户端进行抓包分析，发现评论在这个链接里面，http://m.maoyan.com/mmdb/comments/movie/1200486.json?_v_=yes&offset=1 ，其中1200486是电影的ID，offset是页数；电影的ID我们可以解析http://maoyan.com/films?sortId=3 中的内容得到。<br>
因此我们可以先解析http://maoyan.com/films?sortId=3 得到按评价排行的前300部电影的ID，然后通过ID构造出评论的url： http://m.maoyan.com/mmdb/comments/movie/{movie_id}.json?_v_=yes&offset={offset} 来获取评论。
## 运行环境
<br>解释器：python3.6 </br>
<br>爬虫框架：scrapy  </br>
<br>存储环境：MongoDB </br>
## 结果展示

<br>
![数量](https://github.com/ZZShi/zhihu/blob/master/count.png)
<br>
![详细信息](https://github.com/ZZShi/zhihu/blob/master/detail.png)
