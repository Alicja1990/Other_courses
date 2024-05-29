run:
	python src/my_pyspark.py

install:
	pip install --upgrade pip && \
		pip install -r requirements.txt

format:
	find Pyspark/src -name '*.py' -exec black {} +

lint:
	find Pyspark/src -name "*.py" | xargs pylint --disable=R,C

test:
	python -m pytest -vv test
