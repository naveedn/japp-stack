# Dockerfile needs to be built of the root directory of japp-stack (check build context)

FROM jupyter/datascience-notebook:latest
COPY config/notebook/requirements.txt /home/jovyan/requirements.txt
RUN pip install -r requirements.txt
WORKDIR /home/jovyan/work