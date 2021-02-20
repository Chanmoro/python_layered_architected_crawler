from dataclasses import dataclass
from typing import List

from bs4 import BeautifulSoup


@dataclass(frozen=True)
class ParsedWebPage:
    title: str
    links: List[str]


@dataclass(frozen=True)
class WebPageParser:
    def parse(self, html: str) -> ParsedWebPage:
        soup = BeautifulSoup(html, "html.parser")
        return ParsedWebPage(
            title=self._parse_title(soup),
            links=self._parse_links(soup),
        )

    def _parse_title(self, soup: BeautifulSoup) -> str:
        return soup.select_one('title').get_text(strip=True)

    def _parse_links(self, soup):
        return [a['href'] for a in soup.select('a')]
