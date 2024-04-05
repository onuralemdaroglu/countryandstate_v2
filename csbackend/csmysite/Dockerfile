FROM python:3-alpine

# The enviroment variable ensures that the python output is set straight
# to the terminal with out buffering it first
ENV PYTHONUNBUFFERED 1

WORKDIR /app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

VOLUME /app

COPY . .
CMD [ "python", "manage.py", "runserver", "0.0.0.0:8000" ]
EXPOSE 8000