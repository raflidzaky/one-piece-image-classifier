from PIL import Image
import io

def display_image(image_file):
    '''
        This function will return the file as an image (that will be displayed).
        The input itself is an image that users have submitted.
    '''
    image_bytes = image_file.read()    
    image = Image.open(io.BytesIO(image_bytes))
    return image