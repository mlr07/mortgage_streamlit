FROM python:3.8-slim

WORKDIR /usr/app/src

COPY requirements.txt requirements.txt

RUN pip install --no-cache-dir -r requirements.txt

COPY app/ ./

EXPOSE 80

# ENTRYPOINT [ "streamlit", "run", "src/app.py", \
#              "--browser.serverAddress", "0.0.0.0" \
#              "--server.enableCORS", "False", \
#              "server.port", "80"]

CMD ["sh", "-c", "streamlit run --browser.serverAddress 0.0.0.0 --server.enableCORS False --server.port 80 /usr/app/src/main.py" ]

