from unittest import TestCase
from unittest.mock import Mock

from crawler.domain.web_page import WebPage
from crawler.repositories.json_repository import JsonRepository
from crawler.requester.web_page_requester import WebPageRequester
from crawler.usecases.collect_links import CollectLinks


class CollectLinksTest(TestCase):
    def test_exec(self):
        requester_mock = Mock(spec=WebPageRequester)
        requester_mock_data = {
            'http://test/1': WebPage(url='http://test/1', title='test 1', links=['http://test/1-1', 'http://test/1-2']),
            'http://test/1-1': WebPage(url='http://test/1-1', title='test 1-1', links=['http://test/1-1-1']),
            'http://test/1-2': WebPage(url='http://test/1-2', title='test 1-2', links=[]),
            'http://test/1-1-1': WebPage(url='http://test/3', title='test 1-1-1', links=[]),
        }
        requester_mock.get_page.side_effect = lambda url: requester_mock_data[url]

        repository_mock = Mock(spec=JsonRepository)

        usecase = CollectLinks(
            requester=requester_mock,
            repository=repository_mock,
        )
        usecase.exec(seed_url='http://test/1', depth=3)

        self.assertEqual(repository_mock.add.call_count, 4)
