from scrapy import spiderloader


# prepare crawlers with their corresponding target urls into a list i.e,  [<spider>, <url>]
def get_urls(sites, classes):
    for spider, class_name in classes:
        objects = sites.objects.filter(spider=spider).all()
        for obj in objects:
            if obj.spider == spider:
                yield [class_name, obj.site_url, obj.site_id, obj.status]


# get all spiders and spider classes
def match_spiders(target_sites, settings):
    spider_loader = spiderloader.SpiderLoader.from_settings(settings)
    spiders = spider_loader.list()
    spider_classes = [[name, spider_loader.load(name)] for name in spiders]
    yield get_urls(target_sites, spider_classes)
