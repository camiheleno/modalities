import datetime
from bson.json_util import dumps
from flask import Flask
from flask import request
from flask import jsonify
from pymongo import MongoClient, DESCENDING
import sys

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hey I'm using Docker!"

@app.route('/modalities', methods = ['GET'])
def get_modalities():
    status_code = 200
    json_response = {}
    if 'modalidade' not in request.args:
        json_response = {'code': 2, 'status': 'error', 'message': 'No modality was informed.'}
        status_code = 500
    elif 'data_inicio' not in request.args: 
        json_response = {'code': 3, 'status': 'error', 'message': 'No inital date was informed.'}
        status_code = 500
    elif 'data_fim' not in request.args: 
        json_response = {'code': 4, 'status': 'error', 'message': 'No final date was informed.'}
        status_code = 500

    if status_code != 500:
        client = MongoClient('142.44.178.41', 27017)
        db = client.camilla
        collection = db.estudantes

        final_date = datetime.datetime.strptime(request.args['data_fim'], '%Y-%m-%d')
        initial_date = datetime.datetime.strptime(request.args['data_inicio'], '%Y-%m-%d')

        print(final_date, file=sys.stderr)
        print(initial_date, file=sys.stderr)
        modalities = collection.find(
            {
                "modalidade": request.args['modalidade'].upper(),
                "data_inicio": {"$lte": final_date, "$gte": initial_date}
            },
            { "_id":0, "nome": 1, "idade_ate_31_12_2016": 1, "ra": 1, "campus": 1, "municipio": 1, "curso": 1, "modalidade": 1, "nivel_do_curso": 1, "data_inicio": 1 }
        ).sort("data_inicio", DESCENDING)

        json_response = {'code': 1, 'status': 'success', 'data': list(modalities)}

    resp = jsonify(json_response)
    resp.status_code = status_code

    return resp

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
