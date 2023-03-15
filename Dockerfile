FROM python:3.8.5
COPY requirements.txt /code/requirements.txt
COPY .  /code
WORKDIR /code
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt
EXPOSE 8000
CMD ["uvicorn", "main:app", "--host", "127.0.0.1", "--port", "8000"]