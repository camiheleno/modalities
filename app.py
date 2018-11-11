import datetime
from flasgger import Swagger
from flasgger.utils import swag_from
from flask import Flask
from flask import request
from flask import jsonify
from pymongo import MongoClient
import sys

app = Flask(__name__, instance_relative_config=True)
app.config.from_envvar('APP_CONFIG_FILE')
Swagger(app)

@app.route("/")
def hello():
    return "Hey I'm using Docker!"

@app.route('/modalities', methods = ['GET'])
@swag_from('docs/get_modalities.yml')
def get_modalities():
    try:
        status_code = 200
        json_response = {}
        if 'modalidade' not in request.args:
            json_response = {'code': 2, 'status': 'error', 'message': 'No modality was informed.'}
            status_code = 400
        elif 'data_inicio' not in request.args: 
            json_response = {'code': 3, 'status': 'error', 'message': 'No inital date was informed.'}
            status_code = 400
        elif 'data_fim' not in request.args: 
            json_response = {'code': 4, 'status': 'error', 'message': 'No final date was informed.'}
            status_code = 400

        if status_code != 400:
            client = MongoClient(app.config['MONGO_HOST'], app.config['MONGO_PORT'])
            collection = client.camilla.estudantes

            final_date = datetime.datetime.strptime(request.args['data_fim'], '%Y-%m-%d')
            initial_date = datetime.datetime.strptime(request.args['data_inicio'], '%Y-%m-%d')

            modalities = collection.find(
                {
                    "modalidade": request.args['modalidade'].upper(),
                    "data_inicio": {"$lte": final_date, "$gte": initial_date}
                },
                { "_id":0, "nome": 1, "idade_ate_31_12_2016": 1, "ra": 1, "campus": 1, "municipio": 1, "curso": 1, "modalidade": 1, "nivel_do_curso": 1, "data_inicio": 1 }
            ).sort("data_inicio", -1)

            json_response = {'code': 1, 'status': 'success', 'data': list(modalities)}

        resp = jsonify(json_response)
        resp.status_code = status_code
    except:
        resp = jsonify({'code': 99, 'status': 'error', 'message': sys.exc_info()[0]})
        resp.status_code = 500
    finally:
        return resp
        

@app.route('/courses', methods = ['GET'])
@swag_from('docs/get_courses.yml')
def get_courses():
    try:
        status_code = 200
        json_response = {}
        if 'campus' not in request.args:
            json_response = {'code': 5, 'status': 'error', 'message': 'No campus was informed.'}
            status_code = 400

        if status_code != 400:
            client = MongoClient(app.config['MONGO_HOST'], app.config['MONGO_PORT'])
            collection = client.camilla.estudantes

            courses = collection.find(
                {
                    "campus": request.args['campus'].upper()
                }
            ).distinct("curso")

            json_response = {'code': 1, 'status': 'success', 'data': list(courses)}

        resp = jsonify(json_response)
        resp.status_code = status_code
    except Exception as e:
        resp = jsonify({'code': 99, 'status': 'error', 'message': e})
        resp.status_code = 500
    finally:
        return resp

if __name__ == "__main__":
    app.run(debug=True)
