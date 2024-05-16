import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import functions as FN  # Import your functions module
import os  # Import the 'os' module (if needed)


# Main program
def main():
    # Create the main window
    ventana = tk.Tk()
    ventana.geometry('1000x1000')
    ventana.title('Entradas automaticas k3')
    ventana.config(bg="white")  # Change "lightblue" to your desired color


    # Creating a restart button
    boton_reiniciar = ttk.Button(ventana, text='Reiniciar', command=FN.saludar)
    boton_reiniciar.grid(row=0, column=0, padx=100, pady=20)

    # Creating an exit button
    boton_salir = ttk.Button(ventana, text='Salir', command=ventana.destroy)
    boton_salir.grid(row=0, column=3, padx=100, pady=20)

    # Adding a title label
    etiqueta = tk.Label(ventana, text="¡Entrada Automatica k3!", font=("Arial", 20, "bold"), background="lightblue")
    etiqueta.grid(row=0, column=1, padx=20, pady=20)

    # Loading and displaying the image (if available)
    image_path = "img/logop.png"  # Replace with your actual image path

    if image_path is not None:
        try:
            image = Image.open(image_path)

            # Get original image dimensions
            original_width, original_height = image.size

            # Calculate scaling factor to maintain aspect ratio
            new_width = 460  # Adjust as needed
            new_height = 460
            width_scale = new_width / original_width
            height_scale = width_scale  # Preserve aspect ratio

            # Adjust height if necessary to fit within label dimensions
            if height_scale * original_height > new_height:
                height_scale = new_height / original_height

            # Resize image with calculated scaling factor
            resized_image = image.resize((int(original_width * width_scale), int(original_height * height_scale)), Image.BILINEAR)

            imagen_tk = ImageTk.PhotoImage(resized_image)

            # Create and configure image label using grid
            etiqueta_imagen = tk.Label(ventana, image=imagen_tk, width=new_width, height=new_height, anchor=tk.CENTER)
            etiqueta_imagen.grid(row=2, column=1, padx=20, pady=20)

        except Exception as e:
            print(f"Error loading image: {e}")

    #condicionar para variar seleccionando el ultimo registro

    #llamado a la funcion que pondra la imagen chiquita durante 5 segundos  luego que estuvo 8 segundos en grande.
 

    # Main loop
    ventana.mainloop()

if __name__ == "__main__":
    main()
