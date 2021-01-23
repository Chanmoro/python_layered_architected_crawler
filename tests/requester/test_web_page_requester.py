from collections import namedtuple
from unittest import TestCase
from unittest.mock import Mock

import requests

from crawler.requester.parser.wab_page_parser import ParsedWebPage, WebPageParser
from crawler.requester.web_page_requester import WebPageRequester


class WebPageRequesterTest(TestCase):
    def test_get_page(self):
        requests_mock = Mock(spec=requests)
        Response = namedtuple('Response', ['url', 'text'])
        requests_mock.get.return_value = Response(
            url='http://example.com/test/response',
            text='test_html',
        )

        parser_mock = Mock(spec=WebPageParser)
        parser_mock_data = {'test_html': ParsedWebPage(
            title='test page title',
            links=['/relative_url', 'http://test.com/absolute_url']
        )}
        parser_mock.parse.side_effect = lambda html: parser_mock_data[html]

        requester = WebPageRequester(
            requests=requests_mock,
            parser=parser_mock,
        )

        result = requester.get_page('http://example.com/test')

        self.assertEqual(result.url, 'http://example.com/test/response')
        self.assertEqual(result.title, 'test page title')
        self.assertEqual(len(result.links), 2)
        self.assertIn('http://test.com/absolute_url', result.links)
        self.assertIn('http://example.com/relative_url', result.links)
