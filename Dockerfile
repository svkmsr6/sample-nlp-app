# 
FROM python:3.9

# 
WORKDIR /code

# 
COPY ./requirements.txt /code/requirements.txt

# 
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

# 
COPY ./ /code/

#
 CMD ["python", "app.py"]
# CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8080"]
# CMD [ "gunicorn", "-w", "4," "-k", "uvicorn.workers.UvicornWorker",  "app:app",  "--timeout", "600"]
# CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]
