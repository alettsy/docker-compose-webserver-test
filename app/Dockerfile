FROM python:3-onbuild
WORKDIR /usr/src/app
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
COPY . .
CMD ["python", "main.py"]