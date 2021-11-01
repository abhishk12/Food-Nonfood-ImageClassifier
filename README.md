# Introduction

The aim of this project is to classify images as a **Food image** or **Non-food** image. The model checks if there is any food product in the image or not. The algorithm used for the binary classification is Convolutional Neural Network (CNN). Training of the model was done on **[Google Colab](https://colab.research.google.com/ "Google Colab")** using GPU runtime and deployed on **[Heroku](https://www.heroku.com/ "Heroku")** which is a free platform as a service (PaaS) cloud platform to deploy, manage, and scale modern apps. The accuracy of the model is around **`86%`**.

# Dataset
The dataset used for the project is [Food-5K](https://www.epfl.ch/labs/mmspg/downloads/food-image-datasets/  "Food-5K dataset link"). This is a dataset containing 2500 food and 2500 non-food images. The whole dataset is divided in three parts: training, validation and evaluation. The naming convention is as follows:

> {ClassID}_{ImageID}.jpg

> ClassID: 0 or 1; 0 means non-food and 1 means food. 

> ImageID: ID of the image within the class. 

_I downloaded the whole dataset and uploaded on google drive so that I can access it through my Google Colab account._

# Preparing Dataset
The images from the raw dataset were of different sizes. To feed the images to CNN, the images should be of same size. As preprocessing step, I resized all the images to a shape of `( 64, 64, 3 )` and divided all the images into train, validation and evaluation dataset. Finally all these numpy arrays were saved in the format of `hdf5` file format so that I can load it anytime and start working on that instead of loading the whole dataset again. 

# Modelling

Keras' Sequential API is the easiest way to model any deep learning model. I have implemented 3 convolutional layers and a dense layer at last which uses sigmoid function.
### Model architecture

<img width="500" alt="model_summary" src="https://user-images.githubusercontent.com/65041091/139639562-066f99a3-835c-4c26-98dc-03a733dae0c6.PNG">

# Training
The model was trained for `12 epochs` for `batch size = 32`. Training accuracy was found to be **`97.53%`** or training error of **`2.47%`**
# Evaluation
The model was evaluated on evaluation data and accuracy was found to be **`86.69%`**. Here we can clearly see that there is **variance problem** as there is a difference of about `10.84%`. This problem can further be improved tuning regularization parameters and using resnets.  
# Deployment
Finally I deployed my model on free deploying service provided by **[Heroku](https://www.heroku.com/ "Heroku")**.
