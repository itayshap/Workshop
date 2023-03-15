FROM python:3.8.5
COPY requirements.txt /code/requirements.txt
COPY .  /code
WORKDIR /code
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt
EXPOSE 8000
CMD ["uvicorn", "main:app", "--host", "localhost", "--port", "8000"]