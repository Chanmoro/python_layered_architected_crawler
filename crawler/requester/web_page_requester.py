import dataclasses
import urllib.parse
from typing import Protocol

import requests

from crawler.domain import WebPage, Url
from crawler.requester.parser.wab_page_parser import WebPageParser


class Requests(Protocol):
    def get(self, url: str) -> requests.models.Response:
        ...


@dataclasses.dataclass(frozen=True)
class WebPageRequester:
    # NOTE: モジュールのインターフェースを protocol で定義するのは mypy では未対応のためエラーを無視する
    # https://www.python.org/dev/peps/pep-0544/#modules-as-implementations-of-protocols
    requests: Requests = requests  # type: ignore
    parser: WebPageParser = dataclasses.field(default_factory=lambda: WebPageParser())

    def get_page(self, url: Url) -> WebPage:
        response = self.requests.get(url.url)
        parsed_web_page = self.parser.parse(response.text)
        return WebPage(
            url=Url(response.url),
            title=parsed_web_page.title,
            links=[Url(urllib.parse.urljoin(response.url, u)) for u in parsed_web_page.links],
        )
