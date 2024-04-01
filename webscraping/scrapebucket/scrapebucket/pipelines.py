# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

import os
import sys
from pathlib import Path

import django
from itemadapter import ItemAdapter
from runspider import Scrape, TargetSite

sys.path.append(os.path.join(Path(__file__).parents[3], 'webscraping'))
os.environ['DJANGO_SETTINGS_MODULE'] = 'webscraping.settings'
# Use `_async_` for Error: Django: SynchronousOnlyOperation: You cannot call this from an async context - use a thread or sync_to_async
os.environ["DJANGO_ALLOW_ASYNC_UNSAFE"] = "true"
django.setup()


class ScrapebucketPipeline:
    def process_item(self, item, spider):

        items = ItemAdapter(item)

        try:
            domain_name = items.get('domain').split('.')[0]
            target_site_pk = (
                TargetSite.objects.filter(site_id__iexact=domain_name).first().pk
            )

            # save new scrapes
            scrape_data = {
                'target_site_id': target_site_pk,
                'spider': spider.name,
                'category': items.get('category'),
                'unit': items.get('unit'),
                'year': items.get('year'),
                'make': items.get('make'),
                'model': items.get('model'),
                'trim': items.get('trim'),
                'stock_number': items.get('stock_number'),
                'vin': items.get('vin'),
                'vehicle_url': items.get('vehicle_url'),
                'msrp': items.get('msrp'),
                'price': items.get('price'),
                'selling_price': items.get('selling_price'),
                'rebate': items.get('rebate'),
                'image_urls': items.get('image_urls'),
                'images_count': items.get('images_count'),
                'page': items.get('page'),
            }
            scrapes = Scrape(**scrape_data)
            scrapes.save()
        except AttributeError:
            pass

        return item
