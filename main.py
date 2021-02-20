import argparse

from crawler.domain import Url
from crawler.usecases.collect_links import CollectLinks


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--seed_url', type=str, help='crawl url')
    parser.add_argument('--depth', type=int, help='depth of traverse links')
    args = parser.parse_args()

    usecase = CollectLinks()
    usecase.exec(
        seed_url=Url(args.seed_url),
        depth=args.depth,
    )


if __name__ == '__main__':
    main()
