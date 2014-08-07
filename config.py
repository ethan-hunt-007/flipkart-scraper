#Constants

URL_FORMAT = "http://www.flipkart.com/search?q=%s&as=off&as-show=on&otracker=start"

SCROLL_TIMES = 3

MONGO_STORAGE_INPUT_DICT = {
                    'name':'',
                    'price':'',
                    'rating':'',
                    'url':''
                }
REDIS_CRAWLER_KEY = 'crawling_keywords'
REDIS_RECENT_SEARCHES = 'recent_search'
MAX_RECENT_SEARCH_ITEMS = 15

PHANTOM_JS_PATH = './phantomjs/bin/phantomjs'
WEBDRIVER = 'phantomjs'
