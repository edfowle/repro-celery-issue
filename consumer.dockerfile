FROM python:3.7-stretch
ENV APP_PATH=/opt/test
WORKDIR $APP_PATH

COPY . .

RUN pip install -r consumer/requirements.txt
ENV PYTHONPATH "${PYTHONPATH}:$APP_PATH"

WORKDIR "$APP_PATH/shared/tasks"
