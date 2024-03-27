from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/api/v1/test', methods=['GET'])
def test():
    # flask_version = Flask.__version__
    # return jsonify({"flask_version": flask_version}), 200
    return "ok"

if __name__ == '__main__':
    app.run(debug=True,port=5000)
