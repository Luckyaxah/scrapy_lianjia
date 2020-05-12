# scrapy_lianjia
链家租房房源爬虫，爬取给定筛选条件下的房源部分信息。

## 数据持久化
爬取结果通过shelve保存到本地

## 数据转换
将shelve爬取结果通过shelve_to_csv.py转换为csv格式文件

## Spiders

- putuo

    爬取链接写死在代码里，待优化。