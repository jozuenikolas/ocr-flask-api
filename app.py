from flask import Flask, jsonify, request
from ocr import getTextFromImage
import numpy as np
from PIL import Image
from flask_cors import CORS


app = Flask(__name__) 
CORS(app)

@app.route('/ping', methods=['GET'])
def ping():
    return jsonify({"message": 'pong!'})

@app.route("/image", methods=['GET'])
def getImage():
    image = request.files['image']
    img = Image.open(image.stream).convert('RGB') 
    open_cv_image = np.array(img) 
    open_cv_image = open_cv_image[:, :, ::-1].copy() 

    message = getTextFromImage(open_cv_image)
    return jsonify({
        "status": "received",
        "message": message
    })

if __name__ == '__main__':
    app.run(debug=True, port=4000)