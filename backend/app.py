from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app, origins=["http://localhost:3000"])

@app.route('/health')
def health():
    return {'status': 'ok'}

@app.route('/api/hello')
def hello():
    return {'message': 'Hello from Flask backend!'}

@app.route('/api/data', methods=['GET', 'POST'])
def data():
    if request.method == 'GET':
        return {'data': 'Sample data from backend'}
    
    if request.method == 'POST':
        json_data = request.get_json()
        return {'received': json_data, 'status': 'success'}

if __name__ == '__main__':
    app.run(debug=True, port=5001)