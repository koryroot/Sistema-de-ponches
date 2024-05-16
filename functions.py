import os

def change_image_extension_to_png(image_path):
    """
    Changes the extension of an image file to PNG.

    Args:
        image_path (str): The path to the image file.

    Returns:
        str: The new path to the image file with the PNG extension.
    """

    # Check if the image path exists
    if not os.path.exists(image_path):
        raise FileNotFoundError(f"Image file not found: {image_path}")

    # Get the current filename and extension
    filename, extension = os.path.splitext(image_path)

    # Check if the image is already in PNG format
    if extension.lower() == ".png":
        return image_path  # No need to change extension

    # Change the extension to PNG
    new_image_path = f"{filename}.png"

    # Rename the image file to the new path
    os.rename(image_path, new_image_path)

    return new_image_path

# Example usage
# image_path = "kory.jpg"  # Replace with the actual image path
# new_png_path = change_image_extension_to_png(image_path)
# print(f"Image converted to PNG: {new_png_path}")

#condicionar para variar seleccionando el ultimo registro
    
#llamado a la funcion que pondra la imagen chiquita durante 5 segundos  luego que estuvo 8 segundos en grande.
 

def saludar():
    print("saludando")