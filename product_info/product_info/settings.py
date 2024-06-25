
BOT_NAME = 'product_info'

SPIDER_MODULES = ['product_info.spiders']
NEWSPIDER_MODULE = 'product_info.spiders'

ROBOTSTXT_OBEY = True

FEEDS = {
    'output.json': {
        'format': 'json',
        'encoding': 'utf8',
        'store_empty': False,
        'indent': 4,
    },
}