import requests
import scrapy
from bs4 import BeautifulSoup
from ..items import CrawlerItem
import os

class AmazonSpider(scrapy.Spider):
    name = 'amazon'
    start_urls = ['https://www.amazon.in/b?node=16382860031&pf_rd_r=KEA9VSE22MH335031JZB&pf_rd_p=fa25496c-7d42-4f20-a958-cce32020b23e']

    def parse(self,response):
        items = CrawlerItem()
        page = requests.get(AmazonSpider.start_urls[0])
        sp = BeautifulSoup(page.content, 'html.parser')
        product = sp.findAll('div', {'class': '_3wU53n'})
        sp = response.css('div._3e7xtJ')
        rating = sp.css('div.hGSR34::text').extract()
        price = sp.css('._2rQ-NK::text').extract()
        temp = sp.css('._38sUEc span span:nth-child(1)::text').extract()
        No_of_people_give_rating = []
        for x in temp:
            No_of_people_give_rating.append(x.split(' ')[0])
        for i in range(0,len(price)):
            items['product'] = product[i].text
            items['price'] = price[i]
            items['rating'] = rating[i]
            items['No_of_people_give_rating'] = No_of_people_give_rating[i].strip()
            yield items

