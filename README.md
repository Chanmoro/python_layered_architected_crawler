<<<<<<< HEAD
# python_layered_architected_crawler

## How to Run

### Run crawler
```console
$ docker-compose run --rm app bash
$(container) make run seed_url=<crawl target URL> depth=2
```

### Test
```console
$ docker-compose run --rm app bash
$(container) make test
```
