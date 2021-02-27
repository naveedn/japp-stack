# Dockerfile needs to be built of the root directory of japp-stack (check build context)

FROM jupyter/datascience-notebook:latest

# Install Dependencies
USER root
COPY config/notebook/requirements.txt /home/jovyan/requirements.txt
RUN pip install -r /home/jovyan/requirements.txt

# Set up webhook server
RUN mkdir /web
RUN chmod -R 755 /web
COPY config/notebook/notebook-webhook.py /web/webserver.py

# Start Master Process
USER jovyan
WORKDIR /home/jovyan
COPY config/notebook/entrypoint.sh entrypoint.sh
CMD  ["sh", "entrypoint.sh"]