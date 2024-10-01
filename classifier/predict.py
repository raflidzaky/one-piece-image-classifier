# TODO: 
# 1. Make a func to extract class names --> match logits as an extract names
# 2. Make a func to do some prediction which return image labels and its probability
# The flow is here:
# Image is being uploaded and displayed --> API sent it to the pre-processing --> API sent the image tensors to predict
# API sent the predicted label and probability back to landing page...

import torch
from image_preprocess import process_image
from model_build import model
from model_load import model_loader

def predict(input, names, model):
    ''' 
        Predict the class of an image using a trained deep learning model.
    '''
    model.eval()
    with torch.no_grad():
        # Process the image
        img = process_image(input)
        
        # Predict prob and class
        logits = model(img)
        prob   = torch.exp(logits)
        
        top_pr, top_class = prob.topk(k=1, dim=1)
        
        # Convert the indices of top_k to its real name
        return top_pr, top_class