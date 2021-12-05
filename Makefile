test: lint pytest

lint:
	pipenv run black . --check
	pipenv run mypy .

pytest:
	pipenv run pytest
