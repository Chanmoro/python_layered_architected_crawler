import dataclasses

from crawler.components.logger import get_logger
from crawler.repositories.json_repository import JsonRepository
from crawler.requester.web_page_requester import WebPageRequester


@dataclasses.dataclass(frozen=True)
class CollectLinks:
    logger = get_logger(__name__)
    requester: WebPageRequester = dataclasses.field(default_factory=WebPageRequester)
    repository: JsonRepository = dataclasses.field(default_factory=JsonRepository)

    def exec(self, seed_url: str, depth: int):
        self.logger.info(f'seed_url: {seed_url}, depth: {depth}')
        current_depth = 0
        current_depth_urls = [seed_url]

        while current_depth_urls and current_depth < depth:
            next_depth_urls = []
            for url in current_depth_urls:
                self.logger.info(f'get web page. url: {url}')
                web_page = self.requester.get_page(url)
                self.repository.add(web_page)

                for link in web_page.links:
                    next_depth_urls.append(link)

            current_depth_urls = next_depth_urls
            current_depth += 1
