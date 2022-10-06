from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET'])
def hello_world():
    return render_template('index.html')

@app.route('/', method=['POST'])
def predict():
    image_file = request.files['imagefile']

if __name__ == '__main__':
    app.run(port=3000, debug=True)
