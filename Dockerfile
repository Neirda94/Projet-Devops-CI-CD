FROM python:3.8

WORKDIR /web

COPY web.py .


RUN pip install flask

EXPOSE 5000

CMD ["python", "web.py"]