run:
	. venv/bin/activate && python app.py

testes:
	. venv/bin/activate && pytest

env:
	python -m venv venv	