FROM python:3
WORKDIR /usr/src/app
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
#RUN python -m spacy download en_core_web_sm
#RUN pip install ./en_core_web_sm-2.0.0.tar.gz
COPY . .
CMD ["python","app.py"]