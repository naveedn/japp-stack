# This server will be run on the jupyter notebook, where it will call down to jupyter nbconvert
# to execute the notebook from airflow.
import subprocess
from flask import Flask
from flask_restful import reqparse, Resource, Api

parser = reqparse.RequestParser()
parser.add_argument('input_nb', required=True, type=str)
parser.add_argument('output_nb', required=False, type=str)


app = Flask('webserver')
api = Api(app)

HOME_DIR = '/home/jovyan/work/'


class RemoteJupyterExecutor(Resource):
    def get(self):
        return {'hello': 'world'}

    def post(self):
        args = parser.parse_args()
        input_nb = HOME_DIR + args['input_nb']
        output_nb = HOME_DIR + args['output_nb']

        cmd_str = f"jupyter nbconvert --to notebook --execute --output {output_nb} {input_nb}"
        completed_process = subprocess.run(cmd_str, shell=True, check=True)

        return 200


api.add_resource(RemoteJupyterExecutor, '/')

if __name__ == '__main__':
    app.run(debug=True)
