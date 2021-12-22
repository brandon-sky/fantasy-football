install-poetry:
	curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python -

initialize-project:
	poetry config virtualenvs.in-project true
	poetry shell
	poetry install
