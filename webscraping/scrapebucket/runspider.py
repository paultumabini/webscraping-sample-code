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

# import models here as src for pipelines & middlewares
from project.models import *
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
            For this setup, delete the previous scraped data and save for new scraped items.
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
