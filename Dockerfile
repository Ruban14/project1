FROM python:3.8-slim-buster
WORKDIR /project1
COPY . /project1
RUN pip install -r requirements.txt
EXPOSE 8000
ENV DJANGO_SETTINGS_MODULE=project1.settings
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
