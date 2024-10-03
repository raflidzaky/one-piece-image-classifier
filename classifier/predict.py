import torch
from classifier.image_preprocess import image_transform, image_processing

# Categories to map
# Since the class is simple, I think we no need to store it as a .txt yet
# As parsing it may take a longer time
# I store as a dict to access it with class index in prediction
categories = [
    "Ace",
    "Akainu",
    "Brook",
    "Chopper",
    "Crocodile",
    "Franky",
    "Jinbei",
    "Kurohige",
    "Law",
    "Luffy",
    "Mihawk",
    "Nami",
    "Rayleigh",
    "Robin",
    "Sanji",
    "Shanks",
    "Usopp",
    "Zoro"
]

def predict(input, model):
    ''' 
        Predict the class of an image using a trained deep learning model.
        Before returning any prediction, it will load and process the image (using image_preprocess.image_processing)
        and model (using model_build.model for foundational architecture and model_load.model_loader for the weights)
        Input: 
            1. input is the image that users have uploaded in display.button(). Since the image_processing "inherits"
               image_preprocess.image_transform functionality (as I include it within the image_processing), hence no 
               need to call image_transform here.
            2. model that is being used -- basic Convolutional Neural Network architecture.
        Output: 
            1. Top category that is limited to 1 class, since this web just only display a specific character and its 
               information
            2. Top category's probability. This will be used in streamlit_app.character_script to manage edge-cases.

    '''
    model.eval()
    with torch.no_grad():
        # Process the image
        img = image_processing(input=input, transform=image_transform())
        
        # Predict prob and class
        logits = model(img)
        prob   = torch.exp(logits)
        
        top_pr, top_class = prob.topk(k=1, dim=1)
        
        # Convert the indices of top_k to its real name
        return top_pr.item(), categories[top_class.item()]