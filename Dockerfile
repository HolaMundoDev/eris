FROM python:3.9

WORKDIR /app

COPY Pipfile Pipfile.lock ./

RUN pip install pipenv --no-cache-dir && \
pipenv install --system --deploy --ignore-pipfile

COPY . .

CMD ["python", "src/main.py"]