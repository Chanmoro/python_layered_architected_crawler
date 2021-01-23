import os
from unittest import TestCase

from crawler.requester.parser.wab_page_parser import WebPageParser


class WebPageParserTest(TestCase):
    def test_parse(self):
        with open(f'{os.path.dirname(__file__)}/fixture/test_wab_page_parser/test_parse.html') as f:
            test_html = f.read()

        parser = WebPageParser()
        result = parser.parse(test_html)

        self.assertEqual(result.title, 'This is test page!')
        self.assertEqual(len(result.links), 2)
        self.assertIn('/link/relative_url', result.links)
        self.assertIn('http://text.example.com/link/absolute_url', result.links)
