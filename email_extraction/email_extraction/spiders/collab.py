# -*- coding: utf-8 -*-
import scrapy
from scrapy import Spider
from scrapy.http import Request


class CollabSpider(scrapy.Spider):
    name = 'collab'
    allowed_domains = []
    start_urls = ['https://www.collaborativepractice.com/members/']

    def parse(self, response):
        for i in range(362,18725+1):   
            absolute_url = response.urljoin(str(i))
            yield Request(absolute_url, callback=self.parse_profile)

    def parse_profile(self, response):

        # company_name = response.xpath('//*[@id="block-system-main"]/div/div/div/div[2]/h3/text()').extract_first()
        office_phone = response.xpath('//*[@id="block-system-main"]/div/div/div/div[4]/span[2]/text()').extract_first()
        email = response.xpath('//*[@id="block-system-main"]/div/div/div/div[6]/span/a/text()').extract_first()
        if len(email)>1:
             website = response.xpath('//*[@id="block-system-main"]/div/div/div/div[5]/span/a/text()').extract_first()
             address_list = response.xpath('//*[@id="block-system-main"]/div/div/div/div[3]/span/text()').extract()
             # Cleaning address
             address=''
             for i in address_list:
                 address+=str(i)
             address.replace('\n','')

             member_since = response.xpath('//*[@id="block-system-main"]/div/div/div/div[7]/span[2]/text()').extract_first()
             professions = response.xpath('//*[@id="block-system-main"]/div/div/div/div[9]/span/text()').extract_first()
             areas_of_practice = response.xpath('//*[@id="block-system-main"]/div/div/div/div[10]/span[2]/text()').extract_first()
             professional_activities = response.xpath('//*[@id="block-system-main"]/div/div/div/div[12]/span/text()').extract_first()
             undergraduate_education = response.xpath('//*[@id="block-system-main"]/div/div/div/div[13]/span/p/text()[1]').extract_first()
             postgraduate_education = response.xpath('//*[@id="block-system-main"]/div/div/div/div[14]/span/p/text()').extract_first()

             yield{
                 
                 'Office Phone': office_phone,
                 'Email': email,
                 'Website': website,
                 'Address': address,
                 'Member Since': member_since,
                 'Professions': professions,
                 'Area of Practice': areas_of_practice,
                 'Professional Activites': professional_activities,
                 'Undergraduate Education': undergraduate_education,
                 'Postgraduate Education': postgraduate_education
             }
        
        
        
        
        
        
        
        
        