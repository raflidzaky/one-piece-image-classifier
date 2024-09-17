from PIL import Image
import io

def display_image(image_file):
    image_bytes = image_file.read()    
    image = Image.open(io.BytesIO(image_bytes))
    return image