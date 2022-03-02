test-markers-ui:
	poetry run pytest -m ui

test-markers-entertainment:
	poetry run pytest -m entertainment

test-markers-engine:
	poetry run pytest -m engine

test-parametrize:
	poetry run pytest -v ./tests/parametrize

test-data-driven:
	poetry run pytest -v ./tests/data-driven

test-cross-browser:
	poetry run pytest -v -n4 ./tests/cross-browser

test-parallel:
	poetry run pytest -v -nauto ./tests/parallel

test-white-box:
	poetry run python -m pytest -v tests/white-box

tox:
	poetry run tox