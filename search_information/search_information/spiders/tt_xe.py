import scrapy
from search_information.items import SearchInformationItem

class TtXeSpider(scrapy.Spider):
    name = 'tt_xe'
    allowed_domains = ['tuoitre.vn/xe']
    start_urls = []

    def start_requests(self):
        for i in range(1, 201):
            page = 'http://tuoitre.vn/xe/trang-'+str(i)+'.htm'
            self.start_urls.append(page)
        for url in self.start_urls:
            yield scrapy.Request(url, callback=self.parse, dont_filter=True)


    def parse(self, response):
        for item_url in response.css('#content > div > div.list-middle > div > div.w479.fl.stream-home.list-middle-content > div > ul > li > a ::attr(href)').extract():
            yield scrapy.Request(response.urljoin(item_url), callback=self.parse_new, cb_kwargs=dict(url=item_url), dont_filter=True)

    def parse_new(self, response, url):
        item = SearchInformationItem()
        item['path'] = 'https://tuoitre.vn'+url
        item['title'] = response.css('#main-detail > div.w980 > h1 ::text').extract_first()
        item['title'] = item['title'].strip()
        item['time'] = response.css('#main-detail > div.w980 > div ::text').extract_first()
        item['time'] = item['time'].strip()
        content = ""
        for p in response.css('#main-detail-body > p ::text').extract():
            p = p.strip()
            content = content + p + " "
        
        item['content'] = content
        yield item
