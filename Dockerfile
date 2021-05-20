FROM python:3.9

WORKDIR /usr/src/bot

COPY Pipfile Pipfile.lock ./

RUN pip install pipenv --no-cache-dir && \
pipenv install --system --deploy --ignore-pipfile

COPY . .

CMD ["pipenv", "run", "start"]