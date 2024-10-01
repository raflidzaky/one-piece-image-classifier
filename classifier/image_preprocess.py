from PIL import Image
from torchvision import transforms
import streamlit as st

# Start processing images
def image_transform():
    ''' 
        Scales, crops, and normalizes a PIL image for a PyTorch model,
        returns a tensor.
    '''
    # Since the image is already being read, I dont need to read it again here
        
        # Make the transformer
    transform = transforms.Compose([
                                    transforms.Resize((100, 100), antialias=True),
                                    transforms.Grayscale(num_output_channels=3),  # Convert to 3 channels
                                    transforms.ToTensor(),  # Convert to tensor
                                    transforms.Normalize((0.5,), (0.5,)) 
                                    ])
    return transform

def image_processing(input, transform):
    try:
        # Make as a tensor
        img_tensor = transform(input)

        # Unsqueeze as it is needed to feed the image to model
        tensor_fin = img_tensor.unsqueeze(0)
        return tensor_fin

    except Exception as e:
        st.write(f"Error processing image: {e}")
        return None