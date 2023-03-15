FROM python:3.8.5
COPY requirements.txt /code/requirements.txt
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt
EXPOSE 8000
CMD ["uvicorn", "api_app:app", "--host", "0.0.0.0", "--port", "8000"]