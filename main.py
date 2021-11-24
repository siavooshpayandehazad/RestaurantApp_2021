from flask import Flask
from flask import request, jsonify, redirect
from flask_restful import Api, Resource
from flask import render_template, make_response

app = Flask(__name__, template_folder='template', static_url_path='/static')
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = False
api = Api(app)

class main(Resource):
    def get(self):
        headers = {'Content-Type': 'text/html'}
        return make_response(render_template('main.html', arg1="argument 1", arg2="argument 2"),200,headers)

    def post(self):
        print("here in post method")
        req_data = request.json
        print("req_data", req_data)
        result = "results"
        """
        do some things here
        """
        return result, 200


@app.route('/API', methods=['POST'])
def API():
    print("here in API")
    req_data = request.json
    print("req_data", req_data)
    return "data", 200


api.add_resource(main, '/main.html')


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
