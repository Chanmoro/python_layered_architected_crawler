import os

from crawler.requester.parser.wab_page_parser import WebPageParser


class TestWebPageParser:
    def test_parse(self):
        with open(f'{os.path.dirname(__file__)}/fixture/test_wab_page_parser/test_parse.html') as f:
            test_html = f.read()

        parser = WebPageParser()
        result = parser.parse(test_html)

        assert result.title == 'This is test page!'
        assert len(result.links) == 2
        assert '/link/relative_url' in result.links
        assert 'http://text.example.com/link/absolute_url' in result.links
