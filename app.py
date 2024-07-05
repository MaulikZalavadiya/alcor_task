from flask import Flask, jsonify
import requests
import xmltodict

app = Flask(__name__)

@app.route('/', methods=['GET'])
def get_data():
    url = 'https://filesampleshub.com/download/code/xml/sample2.xml'
    response = requests.get(url)
    
    if response.status_code == 200:
        xml_data = response.content
        json_data = xmltodict.parse(xml_data)
        return jsonify(json_data)
    else:
        return jsonify({"error": "Unable to fetch data"}), response.status_code

if __name__ == '__main__':
    app.run(debug=True)

