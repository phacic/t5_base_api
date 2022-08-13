isort:
	isort ./app ./tests

format: isort
	black .

type_check:
	mypy ./app ./tests