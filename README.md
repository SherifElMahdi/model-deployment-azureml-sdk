# Deploying IMDB Reviews Classifier Model using Azure Machine Learning Service

In this GitHub repo, we learn how to deploy a keras model using Azure Machine Learning Service. We will use Microsoft Azure Machine Learning Service to deploy our model as a REST API end point to be consumed/invoked by any client application. [Azure Machine Learning SDK for Python](https://docs.microsoft.com/en-us/python/api/overview/azure/ml/intro?view=azure-ml-py) is used to work with Azure Machine Learning Service.

### What Model are we deploying?
Keras model that classifies IMDB movie reviews into "positive" reviews and "negative" reviews, just based on the text content of the review. This model is developed in Chapter 3, Section 5 of [Deep Learning with Python book](https://www.manning.com/books/deep-learning-with-python?a_aid=keras&a_bid=76564dff) by [François Chollet](https://github.com/fchollet). Check this his GitHub repo to find how the model is developed. (https://github.com/fchollet/deep-learning-with-python-notebooks/blob/master/3.5-classifying-movie-reviews.ipynb)

### Which data set are we using?
The model is developed using IMDB dataset that comes packaged with Keras. Data has already been preprocessed.
