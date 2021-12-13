from flask import Flask, jsonify, request

app = Flask(__name__)
data = [{
    "Contact": "9987644456",
    "name": "XYZ",
    "id": 1,
    "done": False, 
}, 
{
    "Contact": "9876543222",
    "name": "ABC",
    "id": 2 ,
    "done": False, 
}]

@app.route("/")
def helloworld():
    return 'Hello World'

@app.route("/get-data")
def getdata():
    return jsonify({"data": data})

@app.route("/add-data", methods=["POST"])
def addTask():
    if(not request.json):
        return jsonify({
            "status": "error",
            "message": "Please provide the data!"
        }, 400)

    contact = {
        'id': data[-1]['id']+1,
        'Name': request.json['Name'],
        'Contact': request.json.get('Contact', ""),
        'done': False,
    }

    data.append(contact)
    return jsonify({
        "status": "success",
        "message": "Task successfully created"
    })


if __name__ == "__main__": 
    app.run()
