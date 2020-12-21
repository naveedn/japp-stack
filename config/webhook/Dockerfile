# Dockerfile needs to be built of the root directory of japp-stack (check build context)

FROM naveedn/japp_stack:notebook

RUN pip install flask-restful gunicorn
EXPOSE 3000

USER root
RUN mkdir /web
RUN chmod -R 755 /web
WORKDIR /web

COPY config/webhook/notebook-webhook.py webserver.py
COPY config/webhook/entrypoint.sh entrypoint.sh

USER jovyan
ENTRYPOINT ["sh", "./entrypoint.sh" ]