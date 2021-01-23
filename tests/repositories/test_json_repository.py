import shutil
from textwrap import dedent
from unittest import TestCase

from crawler.domain.web_page import WebPage
from crawler.repositories.json_repository import JsonRepository


class JsonRepositoryTest(TestCase):
    def tearDown(self) -> None:
        shutil.rmtree('/tmp/test_crawler/')

    def test_add(self):
        repository = JsonRepository(
            output_dir='/tmp/test_crawler/',
        )

        repository.add(WebPage(url='http://test.com/1', title='test page 1', links=['http://test.com/1-1']))
        repository.add(WebPage(url='http://test.com/2', title='test page 2', links=[]))

        with open('/tmp/test_crawler/output.jsonl') as f:
            test_json = f.read()

        self.assertEqual(test_json, dedent("""\
        {"url": "http://test.com/1", "title": "test page 1", "links": ["http://test.com/1-1"]}
        {"url": "http://test.com/2", "title": "test page 2", "links": []}
        """))
