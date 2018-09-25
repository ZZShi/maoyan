# -*- coding: utf-8 -*-
import json
import scrapy
from maoyan.items import MaoyanItem


class CommentSpider(scrapy.Spider):
    name = 'comment'
    allowed_domains = ['maoyan.com']
    base_url = 'http://maoyan.com/films?showType=3&sortId=3&offset={offset}'
    detail_url = 'http://m.maoyan.com/mmdb/comments/movie/{movie_id}.json?_v_=yes&offset={offset}'

    def start_requests(self):
        for page in range(0, 10):
            url = self.base_url.format(offset=str(page * 30))
            yield scrapy.Request(url, callback=self.parse)

    def parse(self, response):
        for movie in response.css('.movie-list dd'):
            movieName = movie.css('.channel-detail::attr(title)').extract_first()
            movieId = movie.css('.channel-detail a::attr(data-val)').extract_first()[9: -1]
            for offset in range(1, 1001):
                yield scrapy.Request(self.detail_url.format(movie_id=movieId, offset=str(offset)),
                                     callback=self.parse_detail, meta={'movieName': movieName, 'movieId': movieId})

    def parse_detail(self, response):
        results = json.loads(response.text).get('cmts')
        movieName = response.meta.get('movieName')
        movieId = response.meta.get('movieId')
        for result in results:
            item = MaoyanItem()
            item['movieName'] = movieName
            item['movieId'] = movieId
            for field in item.fields:
                if field in result.keys():
                    item[field] = result.get(field)
            yield item
