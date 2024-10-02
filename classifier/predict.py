import torch
from image_preprocess import image_transform, image_processing

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