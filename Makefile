run:
	. venv/bin/activate && python app.py

run_tests:
	. venv/bin/activate && pytest
	
requirement:
	. venv/bin/activate && pip3 install -r requirements.txt

env:
	python3.8 -m venv venv	