## 这是一个分页工具，对于大量数据的分页展示比较适用效果如图

## 下面以Django里的运用为例
* views.py 里的test是一个视图函数，return_data为所有数据，这里用python生成数据
* page.py里面有个Pagination类，是分页的主要部分
* show_data.html为页面展示部分，主要内容是一个表格
* pagination.html是分页部分

![](http://p1.bqimg.com/567571/4b038de18fe88510.jpg)
![](http://i1.piimg.com/567571/c191c9c0d7d116a4.jpg)
