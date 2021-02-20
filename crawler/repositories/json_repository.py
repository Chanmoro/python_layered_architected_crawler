import dataclasses
import json
import os

from crawler.domain import WebPage


@dataclasses.dataclass(frozen=True)
class JsonRepository:
    output_dir: str = './'
    output_filename: str = 'output.jsonl'

    def __post_init__(self):
        os.makedirs(self.output_dir, exist_ok=True)
        if not os.path.exists(self.output_filepath):
            return
        os.remove(self.output_filepath)

    @property
    def output_filepath(self):
        return os.path.join(self.output_dir, self.output_filename)

    def add(self, web_page: WebPage):

        with open(self.output_filepath, mode='a') as f:
            f.write(json.dumps(web_page.to_dict()))
            f.write('\n')
