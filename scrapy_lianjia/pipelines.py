# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import shelve
from scrapy.exceptions import DropItem


class ScrapyLianjiaPipeline(object):
    def process_item(self, item, spider):
        return item

class ShelveWriterPipeline(object):
    def process_item(self, item, spider):
        if item.get('房源Id'):
            if not item['房源Id'] in self.dbase:
                self.dbase[item['房源Id']] = dict(item)
                return item
            else:
                raise DropItem("Duplicate item found: %s" % item)
        else:
            raise DropItem('Missing Id in %s' % item)
            

    def open_spider(self, spider):
        print('This method is called when the spider is opened')
        self.dbase = shelve.open('./mydbase')
        
    
    def close_spider(self, spider):
        self.dbase.close()
        print('This method is called when the spider is closed')
