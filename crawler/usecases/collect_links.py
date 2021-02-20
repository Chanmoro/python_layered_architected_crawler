import dataclasses

from crawler.components.logger import get_logger
from crawler.domain import Url
from crawler.repositories.json_repository import JsonRepository
from crawler.requester.web_page_requester import WebPageRequester


@dataclasses.dataclass(frozen=True)
class CollectLinks:
    logger = get_logger(__name__)
    requester: WebPageRequester = dataclasses.field(default_factory=lambda: WebPageRequester())
    repository: JsonRepository = dataclasses.field(default_factory=lambda: JsonRepository())

    def exec(self, seed_url: Url, depth: int):
        self.logger.info(f'seed_url: {seed_url}, depth: {depth}')
        current_depth = 0
        current_depth_urls = [seed_url]

        while current_depth_urls and current_depth < depth:
            next_depth_urls = []
            for url in current_depth_urls:
                if seed_url.domain != url.domain:
                    self.logger.info(f'Ignore domain which is different from the seed url domain. url: {url}')
                    continue

                self.logger.info(f'Crawl web page. target url: {url}')
                web_page = self.requester.get_page(url)
                self.repository.add(web_page)

                for link in web_page.links:
                    next_depth_urls.append(link)

            current_depth_urls = next_depth_urls
            current_depth += 1
