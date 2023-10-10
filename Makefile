TARGET = main.py

run:
	python ./src/$(TARGET)

test:
	coverage run -m pytest
	coverage html
