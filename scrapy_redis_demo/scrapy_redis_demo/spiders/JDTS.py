import scrapy
import json
from scrapy_redis_demo.items import ScrapyRedisDemoItem
from copy import deepcopy
from scrapy_redis.spiders import RedisSpider


class JdtsSpider(RedisSpider):
    # 设置分步式爬虫执行键
    name = 'JDTS'
    # allowed_domains = ['jd.com']
    # start_urls = ['https://pjapi.jd.com/book/sort?source=bookSort&callback=jsonp_1655389512259_38385']

    redis_key = 'book'

    # 获取京东图书分类页面，进行数据分析
    def parse(self, response, **kwargs):
        # 获取页面json数据，并进行格式优化
        html_data = response.text.replace('jsonp_1655389512259_38385(', '').replace('}]}]})', '}]}]}')
        data = json.loads(html_data)
        items = ScrapyRedisDemoItem()
        # 遍历json数据
        for fatherlist in data["data"]:
            # 提取分类名称
            items["categoryName"] = fatherlist["categoryName"]
            # 提取分类id
            fatherCategoryId = int(fatherlist["fatherCategoryId"])
            # 提取子类id
            categoryId = int(fatherlist["categoryId"])
            # 提取子类列表
            sonList = fatherlist["sonList"]
            for son in sonList:
                # 取得最小标题
                items["sonCategoryName"] = son["categoryName"]
                # 提取最小标题id
                sonCategoryId = int(son["categoryId"])
                # 拼接三个id组合成详细页url
                infourl = 'https://list.jd.com/list.html?cat={},{},{}'.format(fatherCategoryId,
                                                                              categoryId,
                                                                              sonCategoryId)
                yield scrapy.Request(url=infourl, callback=self.re_data, meta={"items": deepcopy(items)})

    # 解析详细页url数据
    def re_data(self, response):
        items = response.meta["items"]
        data_list = response.xpath('//*[@id="J_goodsList"]/ul/li')
        for data in data_list:
            # 提取书本名称、价格、出版社
            items["bookName"] = ''.join(data.xpath('./div[1]/div[3]/a/em/text()').extract_first())
            items["price"] = ''.join(data.xpath('./div[1]/div[2]/strong/i/text()').extract())
            items["press"] = ''.join(data.xpath('./div[1]/div[6]/a/text()').extract())
            yield items
