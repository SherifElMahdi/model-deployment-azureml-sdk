# Deploying IMDB Reviews Classifier Model using Azure Machine Learning Service

In this GitHub repo, we learn how to deploy a keras model using Azure Machine Learning Service. We will use Microsoft Azure Machine Learning Service to deploy our model as a REST API end point to be consumed/invoked by any client application. [Azure Machine Learning SDK for Python](https://docs.microsoft.com/en-us/python/api/overview/azure/ml/intro?view=azure-ml-py) is used to work with Azure Machine Learning Service.

### Note:
If you reached this GitHub repo from ["Developing and Deploying a Churn Prediction Model with Azure Machine Learning Services" blog post](https://www.microsoft.com/developerblog/2018/12/06/develop-and-deploy-a-hybrid-multi-input-churn-prediction-model-with-azure-machine-learning-services/), you will find here all the explained deployment steps/notebooks. The only difference here is the model file; in this repo we are deploying a reviews classifier model instead of a churn predicition model.

### What Model are we deploying?
Keras model that classifies IMDB movie reviews into "positive" reviews and "negative" reviews, just based on the text content of the review. This model is developed in Chapter 3, Section 5 of [Deep Learning with Python book](https://www.manning.com/books/deep-learning-with-python?a_aid=keras&a_bid=76564dff) by [François Chollet](https://github.com/fchollet). Check his GitHub repo to find how the model is developed. (https://github.com/fchollet/deep-learning-with-python-notebooks/blob/master/3.5-classifying-movie-reviews.ipynb)

Check the repo files to find the model, it's named "BestModel.h5".

### Which data set are we using?
The model is developed using IMDB dataset that comes packaged with Keras. Data has already been preprocessed.

### Prerequisites 
01. Azure Subscription. Don't have? [Create your Azure Subcription from here](https://azure.microsoft.com/en-us/free/?v=18.45)
02. Python 3.3 or greater. Don't have? [Download & Install Python](https://www.python.org/downloads/)
03. Jupyter Notebook. Don't have? [Download & Install Jupyter Notebook](http://jupyter.org/install)
04. Azure Machine Learning SDK for Python. Don't have? [Install Azure ML Python SDK](https://docs.microsoft.com/en-us/python/api/overview/azure/ml/intro?view=azure-ml-py)
05. Git. Don't have? [Download & Install Local Git](https://git-scm.com/downloads)

If you are lazy to download and install prerequisites, you can use Azure Data Science Virtual Machine (DSVM). DSVM is a pre-configured development/experimentation environment in the Azure cloud that is designed for data science work. [Check it out](https://docs.microsoft.com/en-us/azure/machine-learning/service/how-to-configure-environment#dsvm)

### New to Azure Machine Learning Service? Check out the documentation
- [Azure Machine Learning Service](https://docs.microsoft.com/en-us/azure/machine-learning/service/)

Enjoy it!
