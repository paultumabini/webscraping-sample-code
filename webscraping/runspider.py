import argparse
import os
import sys
from pathlib import Path

import django
from scrapy.crawler import CrawlerRunner
from scrapy.utils.log import configure_logging
from scrapy.utils.project import get_project_settings
from twisted.internet import defer, reactor

sys.path.append(os.path.join(Path(__file__).parents[0], 'scrapebucket'))
sys.path.append(
    os.path.join(Path(__file__).parents[2], 'webscraping')
)  # root directory

os.environ['DJANGO_SETTINGS_MODULE'] = 'webscraping.settings'
django.setup()

# import models here as src for pipelines & middleware as well
from project.models import Scrape, TargetSite
from scrapebucket.urls_crawl import match_spiders

# Run spiders sequentially
configure_logging()
settings = get_project_settings()
runner = CrawlerRunner(settings)


@defer.inlineCallbacks
def crawl(arg):
    for results in match_spiders(TargetSite, settings):
        for spider, url, domain, status in results:
            """
            For this setup, delete previous scraped data and save new scraped items.
            """
            if (
                spider.__name__.lower() == f'{arg.lower()}spider'
                and status.lower() == 'active'
            ):
                scrapes_prev = (
                    TargetSite.objects.filter(site_id__exact=domain)
                    .first()
                    .scrapes.all()
                )
                if scrapes_prev.count():
                    scrapes_prev.delete()
                yield runner.crawl(spider, url=url)
                print(f'Done running: {spider.__name__}')
            if arg.lower() == 'all' and status.lower() == 'active':
                scrapes_prev_all = Scrape.objects.all()
                if scrapes_prev_all.count():
                    scrapes_prev_all.delete()
                yield runner.crawl(spider, url=url)
                print(f'Done running: {spider.__name__}')

    reactor.stop()


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='spider name')
    parser.add_argument(
        '-s',
        '--spider',
        type=str,
        metavar='',
        required=True,
        help='specify the spider, i.e, the domain name',
    )
    args = parser.parse_args()

    crawl(args.spider)
    reactor.run()  # the script will block here until the last crawl call is finished


# Examples of `runner.crawl` concept on loop `runner.crawl(spider, url=url)`:
# from scrapebucket.spiders.dealerinspire import DealerinspireSpider
# from scrapebucket.spiders.nabthat import NabthatSpider
# yield runner.crawl(DealerinspireSpider, url='https://www.taylorcadillac.ca/')
# yield runner.crawl(NabthatSpider, url='https://www.fairleystevensford.com/')
# yield runner.crawl(DealerinspireSpider, url='https://www.rosetownmainline.net/')

# Run on Terminal:
# -- Spider
# python3 runspider.py -s tadavantage
# -- Target Site
# scrapy crawl nabthat -a url=https://www.fairleystevensford.com/
# scrapy crawl dealerinspire -a url=https://www.taylorcadillac.ca/
# scrapy crawl dealerinspire -a url=https://www.yellowknifemotors.com/

# Addt'l Notes:
# The difference of running the file and spider name has underscore ('_'). For example, av_motors:
# $ scrapy crawl av_motors -a url=https://www.griffithsford.ca/
# $ python runspider.py -s avmotors


# spider names:
# spider.__name__ == 'NabthatSpider'
# spider.__name__ == 'DealerInspireSpider'
# spider.__name__.lower() == 'd2cmediaspider'
