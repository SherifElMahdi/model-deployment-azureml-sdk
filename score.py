import keras
import numpy as np
from keras import losses
from keras import metrics
from keras import optimizers
from azureml.core.model import Model
from keras.models import load_model

def vectorize_sequences(sequences, dimension=10000):
    # Create an all-zero matrix of shape (len(sequences), dimension)
    results = np.zeros((len(sequences), dimension))
    for i, sequence in enumerate(sequences):
        results[i, sequence] = 1.  # set specific indices of results[i] to 1s
    return results


#Load the model
def init():   
    global model
     # retreive the path to the model file using the model name
    model_path = Model.get_model_path('BestModel.h5')
    model = load_model(model_path)
    
    model.compile(optimizer=optimizers.RMSprop(lr=0.001),
                  loss=losses.binary_crossentropy,
                  metrics=[metrics.binary_accuracy])
#Score
def run(test_data_np):
    import json
    
    x_test = vectorize_sequences(test_data_np)
    pred = model.predict(x_test)
    return json.dumps(str(pred))

