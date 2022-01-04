import scrapy
from search_information.items import SearchInformationItem

class VanHoaSpider(scrapy.Spider):
    name = 'van_hoa'
    allowed_domains = ['baochinhphu.vn/Van-hoa/249']
    start_urls = []

    def start_requests(self):
        for i in range(1, 501):
            page = 'http://baochinhphu.vn/Van-hoa/249/trang'+str(i)+'.vgp'
            self.start_urls.append(page)
        for url in self.start_urls:
            yield scrapy.Request(url, callback=self.parse, dont_filter=True)


    def parse(self, response):
        for item_url in response.css('#aspnetForm > div.contents.hasshadow.subpage.clearfix > div.maincontents > div.zonelisting > div > p.photo > a ::attr(href)').extract():
            yield scrapy.Request(response.urljoin(item_url), callback=self.parse_new, cb_kwargs=dict(url=item_url), dont_filter=True)

    def parse_new(self, response, url):
        item = SearchInformationItem()
        item['path'] = 'http://baochinhphu.vn'+url
        item['title'] = response.css('#aspnetForm > div.contents.hasshadow.subpage.clearfix > div.maincontents > div.article-header > h1 ::text').extract_first()
        item['title'] = item['title'].strip()
        item['time'] = response.css('#aspnetForm > div.contents.hasshadow.subpage.clearfix > div.maincontents > div.article-header > p ::text').extract_first()
        item['time'] = item['time'].strip()
        content = ""
        
        for p in response.css('#aspnetForm > div.contents.hasshadow.subpage.clearfix > div.maincontents > div.wrap-article.clearfix > div.article-body.cmscontents > p ::text').extract():
            p = p.strip()
            content = content + p + " "
        
        item['content'] = content
        yield item
