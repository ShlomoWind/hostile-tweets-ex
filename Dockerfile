FROM python:3.10-slim
WORKDIR /app
COPY . /app
EXPOSE 8000
RUN pip install --no-cache-dir -r requirements.txt
RUN python -m nltk.downloader vader_lexicon
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
