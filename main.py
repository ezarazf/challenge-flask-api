from flask import Flask, request, jsonify

app = Flask(__name__)

list_temp = []
@app.route('/sensor1', methods=['POST'])
def simpan_data_sensor1():
    if request.method == 'POST':
        body = request.get_json()
        temperature = body['temperature']
        humidity = body['humidity']
        timestamp = body['timestamp']
        list_temp.append({
            'temperature': temperature, 
            'humidity': humidity,
            'timestamp': timestamp
        })
        print("current database : ",list_temp)
        return ({'message': 'Data berhasil disimpan!'})
    
if __name__ == '__main__':
    app.run(debug=True)