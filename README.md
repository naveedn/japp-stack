# JAPP-stack

The Rapid Prototyping stack for data science projects. This repo contains a docker-compose for a connected & pre-configured cluster containing:
 - Jupyter Notebook
 - Apache Airflow
 - Pandas
 - Postgres

## Installation:
 - Install [Docker](https://docs.docker.com/get-docker/)
 - `git clone` the repo
 - `docker pull` to get the docker images installed locally
 - `docker-compose up` to launch the docker stack

 ... And you're ready to go!

 (`docker-compose down` when you're done)

## Important URLs:
 - Airflow: `http://localhost:8080`
 - Jupyter: `http://localhost:8888`

## Writing your first application
After you `docker-compose up`:
1. Go to the [Jupyter Server](http://localhost:8888) and write your first notebook
    - Notebooks allow you to write text, store images, and graphs alongside your code!
    - A notebook is an executable environment that will run your code in little chunks called cells
    - This allows you to prototype quickly, because you get instantenous feedback as you're developing your project
2. Once you have a notebook you are satisfied with and want to schedule it:
    - Go to `src/pipelines` folder to see where all your data workflows are stored
    - Each data pipeline is defined in its own file. These pipelines are called DAGs
    - Each DAG is composed of tasks. We are going to schedule and execute the notebook below
    - you do this by creating a new `run_notebook_operator` instance in the file, and sequencing it with airflow operators `>>` and `<<`
    - You can trigger workflows to start, re-run jobs, etc from the [Airflow Dashboard](http://localhost:8080)
3. Rinse and repeat
## TODO
- Create mechanism to persist state of db indefinitely
    - Thinking about adding docker image layers
    - Potentially db dumps stored in the directory?
- Write Tutorial

## Nice to Haves
- Integrate with DBT for ELT on the postgres system
- Create scraper image

## How to Build:
Build the required images via the following:
    1. `docker build -f config/notebook/Dockerfile . -t naveedn/japp_stack:notebook`
    1. `docker build -f config/webhook/Dockerfile . -t naveedn/japp_stack:webhook`
