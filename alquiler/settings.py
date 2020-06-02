# -*- coding: utf-8 -*-

BOT_NAME = 'alquiler'

SPIDER_MODULES = ['alquiler.spiders']
NEWSPIDER_MODULE = 'alquiler.spiders'

USER_AGENT = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.116 Safari/537.36'

ROBOTSTXT_OBEY = False

TELNETCONSOLE_ENABLED = False

ITEM_PIPELINES = {
    'alquiler.pipelines.AlquilerPipeline': 300,
}

LOG_LEVEL = 'WARNING'
