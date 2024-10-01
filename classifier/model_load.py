import torch

def model_loader(model_path, model):
    try:
        # Load the checkpoint from the specified path
        checkpoint = torch.load(model_path)
        
        # Rebuild the classifier using the loaded parameters
        model.load_state_dict(checkpoint['model_state_dict'])
        return model
    except Exception as e:
        print(f"Error loading model: {e}")
        return None