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

@app.route("/image", methods=['POST'])
def getImage():
    image = request.files['image']
    img = Image.open(image.stream).convert('RGB') 
    open_cv_image = np.array(img) 
    open_cv_image = open_cv_image[:, :, ::-1].copy() 

    response = getTextFromImage(open_cv_image)
    status = "incorrect"
    message = "Envía otra foto"
    if response["fecha"] != 0:
        status = "correct"
        message = "Foto correcta"
    return jsonify({
        "status": status,
        "message": message,
        "response": {
            "edad": response["age"],
            "fechaNacimiento": response["fecha"]
        }
    })

if __name__ == '__main__':
    app.run(debug=True, port=4000)