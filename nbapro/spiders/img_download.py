import scrapy
from nbapro.items import NbaproItem

class ImgDownloadSpider(scrapy.Spider):
    name = 'img_download'
    start_urls = ['https://pbaccess.video.qq.com/trpc.nbacommunity.news.NewsCgi/NewsIndex?column_id=60&last_id=0&page_num=240&tag_id=']

    def parse_detail(self, response):
        detail_dic = response.json()['data'][0]
        name_group = detail_dic['title']
        IMG_dic = detail_dic['cnt_attr']
        item = NbaproItem()
        for n in range(0,20):
            try:
                item['img_url'] = IMG_dic['IMG_{}'.format(str(n))]['img']['imgurl1000']['imgurl']
                #item['img_name'] = name_group + '_' + str(n)
                item['img_name'] = name_group
                yield item
            except:
                break

    def parse(self, response):
        data_json = response.json()
        data_list = data_json['data']['news_info']
        for item in data_list:
            url_group = 'https://pbaccess.video.qq.com/trpc.nbacommunity.news.NewsCgi/NewsInfo?news_id={}&site=nbapic&column='.format(item['news_id'])
            yield scrapy.Request(url=url_group, callback=self.parse_detail)
