import configparser
import logging

from unittest import TestCase
from validators.url import url

from googlespider.spider import GoogleSpider


class SpiderTest(TestCase):
    @classmethod
    def setup_class(cls):
        """Set up test fixtures"""
        cls.logger = logging.getLogger('SpiderTest')
        # Load config
        cls.config = configparser.ConfigParser()
        cls.config.read('config.ini')

    def test_default_country_is_US(self):
        spider = GoogleSpider(
            query="mr boombastic",
            max_results=10,
            results_per_page=100,
            ignore_https_warnings=True)
        assert spider.country == 'us'

    def test_country_not_configured(self):
        with self.assertRaises(Exception) as context:
            GoogleSpider(
                query="mr boombastic",
                country='cdaaa',
                ignore_https_warnings=True)
            self.assertTrue(context.Exception == ValueError)

    def test_default_language_is_en_US(self):
        spider = GoogleSpider(
            query="mr boombastic",
            max_results=10,
            results_per_page=100,
            ignore_https_warnings=True)
        assert spider.language == 'en-US'

    def test_localise_language(self):
        spider = GoogleSpider(
            query="mr boombastic",
            max_results=10,
            country='ca',
            localise=True,
            results_per_page=100,
            ignore_https_warnings=True)
        assert spider.language == 'en-CA'

    def test_request_headers(self):
        headers = {
            'User-Agent': self.config['DEFAULT'].get('user_agent'),
            'Accept': self.config['DEFAULT'].get('accept_header'),
            'Accept-Language': 'en-CA',
            'Accept-Encoding': 'gzip, deflate',
        }
        spider = GoogleSpider(
            query="mr boombastic",
            max_results=10,
            country='ca',
            localise=True,
            results_per_page=100,
            ignore_https_warnings=True)
        assert spider.headers == headers

    def test_request_params_start_index(self):
        spider = GoogleSpider(
            query="mr boombastic",
            max_results=10,
            localise=True,
            results_per_page=100,
            start=100,
            ignore_https_warnings=True)
        assert spider.params['start'] == 100

    def test_request_params_rpp(self):
        spider = GoogleSpider(
            query="mr boombastic",
            results_per_page=50,
            ignore_https_warnings=True)
        assert spider.params['num'] == 50

    def test_request_params_country(self):
        spider = GoogleSpider(
            query="mr boombastic",
            country='ca',
            ignore_https_warnings=True)
        assert spider.params['gl'] == 'ca'

    def test_request_params_min_date(self):
        spider = GoogleSpider(
            query="mr boombastic",
            min_date='01/01/2017',
            ignore_https_warnings=True)
        self.logger.info(spider.params['tbs'])
        assert spider.params['tbs'] == 'cdr:1,cd_min:01/01/2017'

    def test_request_params_max_date(self):
        spider = GoogleSpider(
            query="mr boombastic",
            max_date='30/01/2017',
            ignore_https_warnings=True)
        self.logger.info(spider.params['tbs'])
        assert spider.params['tbs'] == 'cdr:1,cd_max:30/01/2017'

    def test_request_params_min_and_max_date(self):
        spider = GoogleSpider(
            query="mr boombastic",
            min_date='01/01/2017',
            max_date='30/01/2017',
            ignore_https_warnings=True)
        self.logger.info(spider.params['tbs'])
        assert spider.params['tbs'] == 'cdr:1,cd_min:01/01/2017,cd_max:30/01/2017'

    def test_search_domain(self):
        spider = GoogleSpider(
            query="mr boombastic",
            country='ca',
            ignore_https_warnings=True)
        assert spider.domain == 'google.ca'

    def test_result(self):
        spider = GoogleSpider(
            query="mr boombastic",
            max_results=10,
            min_date='01/01/2017',
            max_date='30/01/2017',
            results_per_page=100,
            ignore_https_warnings=True)
        results = spider.crawl()
        assert len(results) == 10

        for result in results:
            # link, title, snippet
            assert len(result) == 3
            assert url(result[0])  # check link is valid url
            assert len(result[1]) > 0  # check title is parsed
            assert len(result[2]) > 0  # check snippet is parsed
