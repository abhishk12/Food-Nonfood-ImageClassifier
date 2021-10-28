from flask import Flask, render_template, request, redirect
import cv2
import os
from werkzeug.utils import secure_filename
import numpy as np
import h5py
from tensorflow import keras

MODEL_PATH = "./model/my_model.h5"

model = keras.models.load_model(MODEL_PATH)


app = Flask(__name__)
app.config["IMAGE_UPLOADS"] = "./static/allimages/uploaded_images/"
app.config["ALLOWED_EXTENSIONS"] = ["png", "jpg", "jpeg"]

def allowed_ext(filename):
    if(filename.split(".")[1] in app.config["ALLOWED_EXTENSIONS"]):
        return True
    return False

@app.route('/')
def home():
    return render_template("index.html")


@app.route("/upload_image", methods = ["POST", "GET"])
def upload_image():
    image_array = "nothing"

    if request.method == "POST":

        if request.files:
            image = request.files["file_name"]

            if image.filename == "":
                return '<html> <script>alert("Please upload image")</script> </html>'
            
            elif allowed_ext(image.filename) == True:
                print("image is in allowd extensions")
            elif allowed_ext(image.filename) == False:
                print("image not in allowed extensions")
                return '<html> <script>alert("Please upload image")</script> </html>'

            filename__ = secure_filename(image.filename)
            image.save(os.path.join(app.config["IMAGE_UPLOADS"], filename__))
            print("Image saved successfully!")

            image_array = cv2.imread(os.path.join(app.config["IMAGE_UPLOADS"], filename__))
            image_array = cv2.resize(image_array, (64, 64))
            image_array = image_array/255.0
            image_array = np.expand_dims(image_array, axis = 0)
            pred_class = model.predict(image_array)
            pred_class = int(np.squeeze(pred_class)*100)

            if(pred_class < 50):
                answer = "Food"
            elif (pred_class >=50):
                answer = "Non-Food"
            
    return render_template("index.html", prediction_text = "Given image is {}".format(answer), filename = "allimages/uploaded_images/"+filename__)           


if __name__ == ('__main__'):
    app.run(debug=True)