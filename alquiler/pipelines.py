# -*- coding: utf-8 -*-
import sqlite3

from scrapy import Spider
from scrapy.utils.log import logger

from alquiler.bot import send_message


def filtr(item):
    return item['price'] < 500


class AlquilerPipeline:
    # noinspection PyMethodMayBeStatic, PyAttributeOutsideInit,PyUnusedLocal
    def open_spider(self, spider):
        self.conn = sqlite3.connect('../../alquiler.db')
        self.cur = self.conn.cursor()
        self.cur.execute('create table if not exists urls (url varchar)')
        self.count = 0

    # noinspection PyUnusedLocal
    def process_item(self, item, spider):
        self.count += 1
        if not filtr(item):
            return
        url = item['url']
        self.cur.execute(
            'select url from urls where url = ?',
            [url]
        )
        exist = self.cur.fetchone()
        if not exist:
            self.cur.execute(
                'insert into urls (url) values (?)',
                [url]
            )
            self.conn.commit()
            msg = url
            send_message(msg)
        return item

    # noinspection PyUnusedLocal
    def close_spider(self, spider: Spider):
        self.cur.close()
        self.conn.close()
        msg = '%s parsed %i items' % (spider.name, self.count)
        if self.count == 0:
            logger.error(msg)
            send_message(msg)
        else:
            logger.warning(msg)
