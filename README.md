# JAPP stack

- **J**upyter Notebook
- **A**pache Airflow
- **P**andas
- **P**ostgres

 This repo is a project skeleton for the people who want to analyze **DATA** and *do science*™, not spend their day setting up ETL pipelines.

## Benefits

- Effortless setup. Just download docker and go
- Realtime Feedback. Any changes you make, you see the output immediately
- Battle-tested. No fancy, bleeding edge tech. Just the good stuff, so you can focus on your idea.
- Encapsulated by design. All the data you ingest, analyze, and generate can be saved to git so you can collaborate with peers

## Why should I use this?

So you can prevent this.

![this person did not use the JAPP stack](https://imgs.xkcd.com/comics/python_environment.png)

## Getting up and Running

1. Install [Docker](https://docs.docker.com/get-docker/)
1. `git clone` the repo
1. `cd japp-stack`
1. `docker build --platform=linux/amd64 -f config/notebook/Dockerfile . -t naveedn/japp_stack:notebook`
1. `docker-compose up` to launch the docker stack

The rest of the steps are the same. After you build the images, you can `docker-compose up`

## Important URLs

- Airflow: `http://localhost:8080`
- Jupyter: `http://localhost:8888`

Connect to your db instance via `psql` with the following command:

- `docker exec -it japp-stack_db_1 psql -U postgres`

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
3. Rinse and repeat. Most companies have data pipelines composed of dozens of tasks. This stack allows you to incrementally build your idea task-by-task.

## Installing new dependencies

| Dependency   | Instructions   |
|--- |--- |
| Airflow   |  Add the dependencies necessary for Airflow in `config/airflow/airflow-requirements.txt` |
| Jupyter   |  1. Go to `config/notebook/requirements.txt` and add the new dependencies to that file <br /> 2. Go to the project root directory <br /> 3. Build a new jupyter notebook image: `docker build -f config/notebook/Dockerfile . -t naveedn/japp_stack:notebook` <br /> 4. On the next docker-compose up, your dependencies will now exist!  |

## Troubleshooting FAQ

> The database keeps crashing when starting. How can I fix?

Delete and re-create the postgres_volumes directory in data. When the postgres image starts up, if there is no data in that location, it will launch the bootstrap script and install whatever configuration files it needs. Note that this will destroy the data in your database; for that reason you should do sqldumps often so that you can restore a snapshot of your database.

## Potential Future work

- Create scraper image
- Integrate with DBT for ELT on the postgres system
