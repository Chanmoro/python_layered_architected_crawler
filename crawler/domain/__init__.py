import dataclasses
from typing import List
from urllib.parse import urlparse


@dataclasses.dataclass(frozen=True)
class Url:
    url: str
    domain: str = dataclasses.field(init=False)

    def __post_init__(self):
        object.__setattr__(self, 'domain', urlparse(self.url).netloc)


@dataclasses.dataclass(frozen=True)
class WebPage:
    url: Url
    title: str
    links: List[Url]

    def to_dict(self) -> dict:
        return dataclasses.asdict(self)
