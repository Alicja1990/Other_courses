FROM python:slim

WORKDIR /app

COPY pyspark_data.csv /app
COPY python_file.py /app

RUN pip install pandas gradio

CMD ["python", "python_file.py"]