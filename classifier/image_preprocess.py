from PIL import Image
from torchvision import transforms

# Start processing images
def process_image(input):
    ''' 
        Scales, crops, and normalizes a PIL image for a PyTorch model,
        returns an Numpy array
    '''
    # Resize the image
    img = Image.open(input, mode='r')
    transform = transforms.Compose([
        transforms.Resize((100, 100), antialias=True),
        transforms.Grayscale(num_output_channels=3),  # Convert to 3 channels
        transforms.ToTensor(),  # Convert to tensor
        transforms.Normalize((0.5,), (0.5,)) 
    ])
    
    # Make as a tensor
    img_tensor = transform(img)

    # Unsqueeze as it is needed to feed the image to model
    tensor_fin = img_tensor.unsqueeze(0)
    return tensor_fin
