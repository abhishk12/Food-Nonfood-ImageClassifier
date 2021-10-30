# Introduction

The aim of this project is to classify images as a **Food image** or **Non-food** image. The model checks if there is any food product in the image or not. The algorithm used for the binary classification is Convolutional Neural Network (CNN). Training of the model was done on [Google Colab](https://colab.research.google.com/ "Google Colab") using GPU runtime and deployed on [Heroku](https://www.heroku.com/ "Heroku") which is a free platform as a service (PaaS) cloud platform to deploy, manage, and scale modern apps. The accuracy of the model is around 86%.

# Dataset
The dataset used for the project is [Food-5K](https://www.epfl.ch/labs/mmspg/downloads/food-image-datasets/  "Food-5K dataset link"). This is a dataset containing 2500 food and 2500 non-food images. The whole dataset is divided in three parts: training, validation and evaluation. The naming convention is as follows:

> {ClassID}_{ImageID}.jpg

> ClassID: 0 or 1; 0 means non-food and 1 means food. 

> ImageID: ID of the image within the class. 

_I downloaded the whole dataset and uploaded on google drive so that I can access it through my Google Colab account._
