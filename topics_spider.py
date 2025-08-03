import scrapy

class TopicsSpider(scrapy.Spider):
    name = "topics"
    start_urls = ["https://www.chinese-tools.com/phrasebook"]

    def start_requests(self):
        headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36'
        }
        for url in self.start_urls:
            yield scrapy.Request(url=url, headers=headers, callback=self.parse) 
    
    
    def parse(self, response):
        topics = response.css('div.page2 a')
        for topic in topics:
            topic_name = topic.css('::text').get().strip()
            topic_url = topic.attrib['href']

            # Follow the link to the topic page
            yield response.follow(
                url=topic_url,
                callback=self.parse_topic_page,
                meta={'topic': topic_name},
                headers={
                     'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36'
                }
            )

    def parse_topic_page(self,response):
        topic = response.meta['topic']

        for li in response.css('ol li'):
            english = li.css('div.ctf_en::text').get()

            #Extract all Chinese characters inside span.ctf_char > div.ctf_cn
            chinese_chars = li.css('span.ctf_char > div.ctf_cn::text').getall()
            chinese_phrase = ''.join(chinese_chars).strip()

            #Extract all Pinyin parts inside span.ctf_char > div.ctf_pinyin
            pinyin_parts = li.css('span.ctf_char > div.ctf_pinyin::text').getall()
            pinyin = ''.join(pinyin_parts).strip()

            yield {
                'topic': topic,
                'english': english,
                'chinese': chinese_phrase,
                'pinyin': pinyin
            }
            