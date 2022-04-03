FROM python:3.9.11-buster

RUN groupadd -g 1000 dev
RUN useradd -u 1000 -ms /bin/bash -g dev dev

RUN mkdir /app
RUN chown -R dev:dev /app
USER dev
WORKDIR /app

COPY . .

RUN pip install -r requirements.txt

ENV PATH="/home/dev/.local/bin:${PATH}"


CMD [ "/bin/sh" ]