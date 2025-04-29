init:
	python -m venv venv
	./venv/Scripts/pip install -r requirements.txt || ./venv/bin/pip install -r requirements.txt
