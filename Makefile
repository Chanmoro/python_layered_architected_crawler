.PHONY: run
run:
	poetry run python ./main.py --seed_url $(seed_url) --depth $(depth)

.PHONY: test
test:
	$(MAKE) mypy && $(MAKE) pytest


.PHONY: mypy
mypy:
	poetry run mypy crawler

.PHONY: pytest
pytest:
	poetry run pytest
