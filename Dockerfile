FROM python:3.9

WORKDIR /source_code

COPY ./source_code/requirements.txt /source_code/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8080"]