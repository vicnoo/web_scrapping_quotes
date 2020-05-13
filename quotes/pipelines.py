# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
#-----------------------using pymongo to insert into mongo db------------------------------
import pymongo

class QuotesPipeline(object):

    def __init__(self):
        self.conn = pymongo.MongoClient(
            'localhost'
            ,27017
        )
        db = self.conn['myQuotes']
        self.collection = db['quotes_tb']

    def process_item(self, item, spider):
        self.collection.insert(dict(item))
        return item


#------------------------------using sqlite3 and mysql.connector to insert into mysql and sqlite3 to store in a db--------------------------
#import sqlite3
# import mysql.connector

# class QuotesPipeline(object):

#     def __init__(self):
#         self.create_connection()
#         self.create_table()


#     def create_connection(self):
#         #self.conn = sqlite3.connect("myQuotes.db")
#         self.conn = mysql.connector.connect(
#             host = 'localhost'
#             ,user = 'vicnoo'
#             ,passwd = 'Otieno@1125'
#             ,database = 'myquotes'
#         )
#         self.curr = self.conn.cursor()


#     def create_table(self):
#         self.curr.execute(""" DROP TABLE IF EXISTS quotes_tb """)

#         self.curr.execute(""" CREATE TABLE quotes_tb(
#              title text
#             ,author text
#              ,tag text
#              ) """)

    
#     def process_item(self, item, spider):
#         self.store_db(item)
#         #print("pipeline " + item['title'] [0])
#         return item


#     def store_db(self, item):
#         self.curr.execute(""" INSERT INTO quotes_tb VALUES (%s,%s,%s)""",(      # in sqlite we use ? instead of %s
#             item['title'] [0]
#             ,item['author'] [0]
#             ,item['tags'] [0]
#         ))
#         self.conn.commit()
