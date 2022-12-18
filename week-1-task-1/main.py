from flask import Flask,jsonify,request
from data import tasks


app = Flask(__name__)

# Get all the records from the json file
@app.route("/get_data/")
def get_alldata():
    return jsonify({'Task':tasks}),200


# Get a single record from the file
@app.route('/get_data/<task_id>/', methods=['get'])
def get_data(task_id):
    task=[]
    for task in tasks:
        if task['id'] ==int(task_id):
            return jsonify({'task':task})
    return jsonify({'Status':"Value is not defined"})


# Inserting the new data to the file
@app.route('/insert_data', methods=['post'])
def addData():
    if not request.json or not 'title' in request.json:
        return jsonify({'Error':"JSON file or Title is not mentioned"}) ,400
    resp_data = request.get_json()
    print (resp_data)
    for task in tasks:
        if task ['id'] == resp_data['id']:
            return jsonify({'Status':"Duplicated"}),400
    tasks.append(resp_data)
    return jsonify({'task': "Added Succesfully"}),201


# modifying the data in the file
@app.route('/new/<int:task_id>', methods=['put'])
def update_task(task_id):
    task = [task for task in tasks if task['id'] == task_id]
    if len(task) == 0:
        return jsonify({'Status': "Error"}), 404

    task[0]['title'] = request.json.get('title', task[0]['title'])
    task[0]['description'] = request.json.get('description', task[0]['description'])
    task[0]['done'] = request.json.get('done', task[0]['done'])
    return jsonify({'Status': "successfully modified"}),200


# Delete the record from the file
@app.route('/delete/<test>', methods=['Delete'])
def del_task(test):
    for task in tasks:
        if task['id'] == int(test):
               tasks.remove(task)
    return jsonify({'outcome': "done with the deletion"}),200


if __name__ == "__main__":
    app.run(debug=True)
