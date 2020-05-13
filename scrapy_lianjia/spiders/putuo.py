# -*- coding: utf-8 -*-
import scrapy
from scrapy_lianjia.items import LianJiaZuFangItem

class PutuoSpider(scrapy.Spider):
    name = 'putuo'
    allowed_domains = ['sh.lianjia.com']
    base_url = 'https://sh.lianjia.com'

    # start_urls = ['https://sh.lianjia.com/zufang/putuo/pg1l0l1brp4000erp5500/']
    def start_requests(self):
        # 此处可以优化
        for i in range(18):
            url = 'https://sh.lianjia.com/zufang/putuo/pg%dl0l1brp4000erp5500/' % i
            yield scrapy.Request(url = url, callback=self.parse)

    def parse(self, response):
        urls = response.xpath("//a[@class='content__list--item--aside']//@href").getall()
        for request_url in urls:
            yield scrapy.Request(url=self.base_url + request_url, callback=self.parse_zufang_page)

    def parse_zufang_page(self, response):
        """租房信息"""
        keys = response.xpath('//ul[@class="content__aside__list"]/li/span/text()').getall()
        values = response.xpath('//ul[@class="content__aside__list"]/li/text()').getall()
        d ={}
        for i,key in enumerate(keys):
            d[key] = values[i]

        item = LianJiaZuFangItem()
        item['房源Id'] = response.url.split('/')[-1].split('.')[0]
        item['价格单位'] = response.xpath('//div[@class="content__aside--title"]/text()').getall()[1].replace('\n','').replace(' ','')
        item['价格'] = response.xpath('//div[@class="content__aside--title"]/span/text()').get()
        item['租赁方式'] = d['租赁方式：']
        item['房屋类型'] = d['房屋类型：'].split()[0]
        item['房屋面积'] = d['房屋类型：'].split()[1]
        item['装修情况'] = d['房屋类型：'].split()[2] if len(d['房屋类型：'].split())>2 else None
        item['朝向'] = d['朝向楼层：'].split()[0]
        item['楼层'] = d['朝向楼层：'].split()[1]
        item['链接'] = response.url
        item['房屋标题'] = response.xpath('//title/text()').get()
        temp = response.xpath('//*[@class="content__article__info2"]/li[@class="fl oneline  "]/text()').getall()
        temp = map(lambda x: x.replace('\n','').replace(' ',''), temp)
        temp = filter(lambda x: x, list(temp))
        item['配套设施_有'] = ';'.join(list(temp))
        temp = response.xpath('//*[@class="content__article__info2"]/li[@class="fl oneline facility_no "]/text()').getall() 
        temp = map(lambda x: x.replace('\n','').replace(' ',''), list(temp))
        temp = filter(lambda x: x, list(temp))
        item['配套设施_无'] = ';'.join(list(temp))
        item['房源维护时间'] = response.xpath('//div[@class="content__subtitle"]/text()').get().strip().split('：')[1]
        yield item
