# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql


class DangdangdemoPipeline(object):
    def process_item(self, item, spider):
        return item


class MySqlPipeline(object):
    # 操作前的准备（打开一个文件夹）
    def open_spider(self, spider):
        self.connction = pymysql.connect("localhost", "gxf", "123456", "gaoxiaofan")
        self.cursor = self.connction.cursor()

    def process_item(self, item, spider):
        # sql语句
        # 测试分支
        sql = "INSERT INTO dangdangwang VALUES(%s,%s,%s,%s,%s,%s,%s,%s)"
        self.cursor.execute(sql, (
            item['book_name'], item['book_price'], item['book_introduction'], item['book_authors'],
            item['book_publishinghouse'], item['book_publisheddate'], item['book_commentsnumbers'],
            item['book_url']))
        self.connction.commit()
        # 将python对象，转换成json串
        return item  # 千万别忘了
    def close_spider(self, spider):
        self.cursor.close()
        self.connction.close()