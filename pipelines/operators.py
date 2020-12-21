from airflow.operators.http_operator import SimpleHttpOperator
import json

def run_notebook_operator(input_nb, output_nb, dag):
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
