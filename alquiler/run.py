from scrapy import spiderloader
from scrapy.crawler import CrawlerProcess
from scrapy.utils import project
from scrapy.utils.log import logger


def run_spiders(spiders: list, settings):
    process = CrawlerProcess(settings=settings)
    for spider in spiders:
        process.crawl(spider)

    process.start()


def main():
    settings = project.get_project_settings()
    spider_loader = spiderloader.SpiderLoader.from_settings(settings)
    spiders = [spider_loader.load(spider) for spider in spider_loader.list()]

    while True:
        run_spiders(spiders, settings)
        logger.warning('sleep for 600 seconds...')


if __name__ == '__main__':
    main()
