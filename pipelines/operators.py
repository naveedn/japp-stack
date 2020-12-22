import json

from airflow.operators.http_operator import SimpleHttpOperator
from airflow.models import Connection
from airflow import (models, settings)


def create_airflow_conn(conf):
    conn = Connection()
    conn.conn_id = conf.get('conn_id')
    conn.conn_type = conf.get('conn_type')
    conn.host = conf.get('host')
    conn.port = conf.get('port')
    conn.login = conf.get('login')
    conn.password = conf.get('password')
    conn.schema = conf.get('schema')
    conn.extra = conf.get('extra')

    session = settings.Session()
    try:
        existing_conns = session.query(Connection).filter(
            Connection.conn_id == conn.conn_id).delete()
    finally:
        session.add(conn)
        session.commit()
    session.close()


def run_notebook_operator(input_nb, output_nb, dag):
    webhook_connection = {
        'conn_id': 'jupyter_webhook',
        'conn_type': 'http',
        'host': 'webhook',
        'port': 3000
    }

    ## HACK: patch bug in puckel/docker
    # passing in connections via env vars does not work so we create an
    # Airflow Connection object manually to satisfy the 'http_conn_id' prop

    create_airflow_conn(webhook_connection)

    return SimpleHttpOperator(
        http_conn_id="jupyter_webhook",
        task_id=f"run_notebook__{input_nb}",
        method="POST",
        endpoint="/",
        data=json.dumps({
            "input_nb": input_nb,
            "output_nb": output_nb,
        }),
        headers={"Content-Type": "application/json"},
        dag=dag
    )
