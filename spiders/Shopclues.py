"""The advent of internet and smartphones has been an impetus to the e-commerce industry. With millions of customers and billions of dollars at stake, the market has started seeing the multitude of players. Which in turn has led to rise of e-commerce aggregator platforms which collect and show you the information regarding your products from across multiple portals? For example when planning to buy a smartphone and you would want to see the prices at different platforms at a single place. What does it take to build such an aggregator platform? Here’s my small take on building an e-commerce site scraper."""

import scrapy

class ShopcluesSpider(scrapy.Spider):
   #name of spider
   name = 'shopclues'

   #list of allowed domains
   allowed_domains = ['https://www.shopclues.com/search?q=mobiles%204g&auto_suggest=1&seq=2&type=keyword&token=mobile&count=8&z=0']
   #starting url
   start_urls = ['https://www.shopclues.com/search?q=mobiles%204g&auto_suggest=1&seq=2&type=keyword&token=mobile&count=8&z=0']
   #location of csv fil


   def parse(self, response):
       #Extract product information
       titles = response.css('img::attr(title)').extract()
       images = response.css('img::attr(data-img)').extract()
       prices = response.css('.p_price::text').extract()
       discounts = response.css('.prd_discount::text').extract()


       for item in zip(titles,prices,images,discounts):
           scraped_info = {
               'title' : item[0],
               'price' : item[1],
               'image_urls' : item[2], #Set's the url for scrapy to download images
               'discount' : item[3]
           }

           yield scraped_info