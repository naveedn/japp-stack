# Dockerfile needs to be built of the root directory of japp-stack (check build context)

FROM naveedn/japp_stack:notebook

USER root
RUN mkdir /web
RUN chmod -R 755 /web
WORKDIR /web

COPY config/webhook/requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY config/webhook/notebook-webhook.py webserver.py
COPY config/webhook/entrypoint.sh entrypoint.sh

USER jovyan
EXPOSE 3000
ENTRYPOINT ["sh", "./entrypoint.sh" ]