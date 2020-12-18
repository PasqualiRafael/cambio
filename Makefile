run:
	. venv/bin/activate && python app.py

testes:
	. venv/bin/activate && pytest

venv:
	python -m venv venv	