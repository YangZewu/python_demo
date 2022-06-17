# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import pymysql
import logging

logger = logging.getLogger(name=__name__)


class ScrapyRedisDemoPipeline:
    coon = None
    cur = None

    def open_spider(self, spider):
        print('爬虫开始')

    def process_item(self, item, spider):
        # 初始化mysql
        self.coon = pymysql.Connect(
            host='116.62.194.29',
            port=3306,
            user='root',
            password='12345678',
            db='mydb',
        )
        self.cur = self.coon.cursor()
        try:
            # 将取得的数据保存到数据库
            print('正在保存{}{}{}'.format(item["categoryName"], item["sonCategoryName"], item["bookName"]))
            sql = 'insert into JDTS(categoryName,sonCategoryName,bookName,price,press) values (%s,%s,%s,%s,%s)'
            params = [(item["categoryName"], item["sonCategoryName"], item["bookName"], item["price"], item["press"])]
            self.cur.executemany(sql, params)
            self.coon.commit()
        except Exception as e:
            # 将异常写入文件
            logger.error(e)
            self.coon.rollback()
        finally:
            self.cur.close()
            self.coon.close()
        return item

    def close_spider(self, spider):
        print('爬虫结束')
