from flask import Flask, request, jsonify
from schedule import insert_data, edit_data,delete_data, insert_data_auto, insert_data_custom,insert_data_daily, insert_data_weekly, insert_data_monthly
from schedule import get_pending_data, update_status

app = Flask(__name__)

@app.route('/', methods=['POST'])
def auto():
    content = request.json
    message, status_code = insert_data_auto(content)
    get_pending_data()
    update_status()
    return jsonify({'message': message}), status_code
@app.route('/insert', methods=['POST'])
def insert():
    content = request.json
    message, status_code = insert_data(content)
    return jsonify({'message': message}), status_code

@app.route('/edit_schedule', methods=['PUT'])
def edit():
    content = request.json
    message, status_code = edit_data(content)
    return jsonify({'message': message}), status_code

@app.route('/delete_schedule/<int:id>', methods=['DELETE'])
def delete(id):
    message, status_code = delete_data(id)
    return jsonify({'message': message}), status_code

@app.route('/insert/daily', methods=['POST'])
def insert_daily():
    content = request.json
    content['schedule_type'] = 'daily'
    message, status_code = insert_data_daily(content)
    return jsonify({'message': message}), status_code

@app.route('/insert/weekly', methods=['POST'])
def insert_weekly():
    content = request.json
    content['schedule_type'] = 'weekly'
    message, status_code = insert_data_weekly(content)
    return jsonify({'message': message}), status_code

@app.route('/insert/monthly', methods=['POST'])
def insert_monthly():
    content = request.json
    content['schedule_type'] = 'monthly'
    message, status_code = insert_data_monthly(content)
    return jsonify({'message': message}), status_code

@app.route('/insert/custom', methods=['POST'])
def insert_custom():
    content = request.json
    content['schedule_type'] = 'custom'
    message, status_code = insert_data_custom(content)
    return jsonify({'message': message}), status_code

if __name__ == '__main__':

    app.run(debug=True)
