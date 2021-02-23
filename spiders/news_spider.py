import scrapy


class NewsSpider(scrapy.Spider):
    name = "news"
    start_urls = [
        "https://seekingalpha.com/market-news",
    ]

    def parsenext(self, response):
        for news in response.css('div._b40cf-r8eI2'):
            print("news", news)

    def parse(self, response):
        for news in response.css('li.item'):
            data = news.css('div.tiny-share-widget::attr(data-tweet)').get()
            if data is not None:
                if data[0] == "$":
                    data_split = data.split("-", 1)
                    snippet = data_split[1].split("https")
                    yield {
                        'title': news.css('h4 a::text').get(),
                        'url': news.css('h4 a::attr(href)').get(),
                        'ticker': data_split[0].strip(),
                        'snippet': snippet[0].strip()
                    }
                else:
                    data_split = data.split("https", 1)
                    snippet = data_split
                    yield {
                        'title': news.css('h4 a::text').get(),
                        'url': news.css('h4 a::attr(href)').get(),
                        'snippet': snippet[0].strip()
                    }

            else:
                pass
