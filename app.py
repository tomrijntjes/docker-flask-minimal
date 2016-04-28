from flask import Flask, make_response,jsonify

"""
Minimal placeholder app for setting up networking
"""



app = Flask(__name__)


@app.route('/',methods=['GET'])
def home():
    return make_response(jsonify({'success': 'DNS records check out'}), 200)
     

if __name__ == "__main__":
    app.run(host='0.0.0.0',port=80)
