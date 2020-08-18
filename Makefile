

venv/Scripts/python.exe:
	py -3 -m venv venv
	venv/Scripts/pip install -r requirements.txt
	venv/Scripts/pip install -e ./flask_toy

devenv: venv/Scripts/python.exe

install: devenv

run: devenv
	venv/Scripts/python.exe run.py

.PHONY: info
info: devenv
	venv/Scripts/pip list