FROM python:3.9.11-buster

RUN groupadd -g 1000 app
RUN useradd -u 1000 -ms /bin/bash -g app app

RUN mkdir /app
RUN chown -R app:app /app
USER app
WORKDIR /app

COPY --chown=app . .

RUN pip install -r requirements.txt

ENV PATH="/home/app/.local/bin:${PATH}"

ENTRYPOINT [ "python" ]

CMD [ "app.py" ]