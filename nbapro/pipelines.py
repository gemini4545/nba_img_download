# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from scrapy.pipelines.images import ImagesPipeline
import scrapy

#class NbaproPipeline:
#    def process_item(self, item, spider):
#        print(item['img_name'],':',item['img_url'])
#        return item

class NbaImgDownloadPipeline(ImagesPipeline):
    def get_media_requests(self, item, info):
        yield scrapy.Request(item['img_url'])

    def file_path(self, request, response=None, info=None, *, item):
        imgname = item['img_name'] + request.url.split('/')[-2]
        #imgname = request.url.split('/')[-2]
        print('{}:下载完成'.format(imgname))
        return imgname

    def item_completed(self, results, item, info):
        return item
