# japp-stack

A Rapid Prototyping stack for data science projects. This repo contains a docker-compose for a connected & pre-configured cluster containing:
 - Jupyter Notebook
 - Apache Airflow
 - Pandas
 - Postgres

## How to use:
 - `git clone` this repo
 - cd into the top-level directory
 - `docker pull`

## Other Notes:
 - Build the required images via the following:
    - `docker build -f config/webhook/Dockerfile . -t naveedn/japp_stack:webhook`
    - `docker build -f config/notebook/Dockerfile . -t naveedn/japp_stack:notebook`


## Snowflakes:
 - the airflow stack has a custom layer. There wasn't an easy way to programmatically add a new connection, so I modified the running container and saved it as a layer ¯\\_(ツ)_/¯
 
