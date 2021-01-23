import dataclasses
from typing import List


@dataclasses.dataclass(frozen=True)
class WebPage:
    url: str
    title: str
    links: List[str]

    def to_dict(self) -> dict:
        return dataclasses.asdict(self)
