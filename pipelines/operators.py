from airflow.operators.http_operator import SimpleHttpOperator
import json

def run_notebook_operator(input_nb=None, output_nb=None, dag):
    return SimpleHttpOperator(
        task_id=f"run_notebook:{input_nb}",
        method="POST",
        endpoint="/",
        data=json.dumps({
        "input_nb": input_nb,
        "output_nb": ouput_nb,
        }),
        headers={"Content-Type": "application/json"},
        dag=dag
    )
