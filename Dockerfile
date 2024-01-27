FROM python:3.10.13

WORKDIR /app

RUN pip install pipenv
COPY Pipfile Pipfile.lock ./

RUN pipenv install --system --deploy

COPY duration_prediction_serve duration_prediction_serve
COPY models/model-2022-01.bin models/model-2022-01.bin

ENV MODEL_FILE=models/model-2022-01.bin
ENV VERSION=2022-01-v0.1

EXPOSE 9696

ENTRYPOINT [ \
    "gunicorn", \ 
    "--bind=0.0.0.0:9696", \ 
    "duration_prediction_serve.serve:app" \ 
]