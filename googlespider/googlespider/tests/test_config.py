import configparser
import logging

from unittest import TestCase

from googlespider.spider import GoogleSpider


class ConfigTest(TestCase):
    @classmethod
    def setup_class(cls):
        """Set up test fixtures"""
        cls.logger = logging.getLogger('ConfigTest')
        # Load config
        cls.config = configparser.ConfigParser()
        cls.config.read('config.ini')

    def test_config_sections_gt_zero(self):
        assert len(self.config.sections()) > 0

    def test_config_contains_domains(self):
        assert len(self.config['Domain']) > 0

    def test_config_contains_languages(self):
        assert len(self.config['Language']) > 0

    def test_config_user_agent(self):
        assert self.config['DEFAULT'].get('user_agent') is not None

    def test_config_accept_header(self):
        assert self.config['DEFAULT'].get('accept_header') is not None
