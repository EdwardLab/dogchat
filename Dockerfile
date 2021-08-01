FROM python:3.9
RUN mkdir /www
WORKDIR /www
ADD . .
RUN pip install -r requirements.txt -i https://mirrors.aliyun.com/pypi/simple && \
    python3 manage.py migrate
CMD ["python3","manage.py","runserver", "0.0.0.0:8000"]
EXPOSE 8000
