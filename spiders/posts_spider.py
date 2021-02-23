import scrapy


class PostSpider(scrapy.Spider):
    name = "posts"
    start_urls = [
        "https://seekingalpha.com/market-news",
    ]

    def parsenext(self, response):
        for post in response.css('div._b40cf-r8eI2'):
            print("post", post)

    def parse(self, response):
        for post in response.css('li.item'):
            data = post.css('div.tiny-share-widget::attr(data-tweet)').get()
            if data is not None:
                if data[0] == "$":
                    data_split = data.split("-", 1)
                    snippet = data_split[1].split("https")
                    yield {
                        'title': post.css('h4 a::text').get(),
                        'url': post.css('h4 a::attr(href)').get(),
                        'ticker': data_split[0].strip(),
                        'snippet': snippet[0].strip()
                    }
                else:
                    data_split = data.split("https", 1)
                    snippet = data_split
                    yield {
                        'title': post.css('h4 a::text').get(),
                        'url': post.css('h4 a::attr(href)').get(),
                        'snippet': snippet[0].strip()
                    }

            else:
                pass
