run:
	@uvicorn recipes.main:app --reload

precommit-install:
	@poetry run pre-commit install

test:
	@poetry run pytest
