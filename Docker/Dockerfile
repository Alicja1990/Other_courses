FROM python:slim

WORKDIR /app

RUN pip install pandas gradio

COPY pyspark_data.csv /app
COPY python_file.py /app

CMD ["python", "python_file.py"]