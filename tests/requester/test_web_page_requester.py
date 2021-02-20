from collections import namedtuple
from unittest.mock import Mock

from crawler.domain import Url
from crawler.requester.parser.wab_page_parser import ParsedWebPage, WebPageParser
from crawler.requester.web_page_requester import WebPageRequester, Requests


class TestWebPageRequester:
    def test_get_page(self):
        requests_mock = Mock(spec=Requests)
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

        result = requester.get_page(Url('http://example.com/test'))

        assert result.url == Url('http://example.com/test/response')
        assert result.title == 'test page title'
        assert len(result.links) == 2
        assert Url('http://test.com/absolute_url') in result.links
        assert Url('http://example.com/relative_url') in result.links
