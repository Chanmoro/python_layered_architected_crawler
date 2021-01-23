import dataclasses
import urllib.parse

import requests

from crawler.domain.web_page import WebPage
from crawler.requester.parser.wab_page_parser import WebPageParser


@dataclasses.dataclass
class WebPageRequester:
    requests: requests = requests
    parser: WebPageParser = dataclasses.field(default_factory=WebPageParser)

    def get_page(self, url: str) -> WebPage:
        response = self.requests.get(url)
        parsed_web_page = self.parser.parse(response.text)
        return WebPage(
            url=response.url,
            title=parsed_web_page.title,
            links=[urllib.parse.urljoin(response.url, url) for url in parsed_web_page.links],
        )
