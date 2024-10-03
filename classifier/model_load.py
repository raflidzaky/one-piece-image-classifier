import torch

def model_loader(model_path, model):
    '''
        This function will load weights to classifier.model_load's architecture. However, to notify bugs, in development,
        I use "try and except". For production, I will not include try and except logic.
    '''
        # Load the checkpoint from the specified path
        # Since I only need the weights, I set the loader to weights only.
    checkpoint = torch.load(model_path, weights_only=True)
        
        # Rebuild the classifier using the loaded parameters
    model.load_state_dict(checkpoint['model_state_dict'])
    return model