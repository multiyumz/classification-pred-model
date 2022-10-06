from flask import Flask, render_template, request

from keras.preprocessing.image import load_img
from keras.preprocessing.image import img_to_array
from keras.applications.vgg16 import preprocess_input
from keras.applications.vgg16 import decode_predictions
from keras.applications.vgg16 import VGG16

app = Flask(__name__)

@app.route('/', methods=['GET'])
def hello_world():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def predict():
    image_file = request.files['imagefile']
    image_path = "./images/" + image_file.filename
    image_file.save(image_path)

    return render_template('index.html')

if __name__ == '__main__':
    app.run(port=3000, debug=True)
