def callit(new_text):
    import tkinter as tk
    from tkinter import PhotoImage
    import ttv

    def update_label():
        label.config(text=new_text)  # Update the text label with the new text
        root.update()
        ttv.videoPlayer(new_text)
    
    # Create the main window
    root = tk.Tk()
    root.title("Image Button and Dynamic Text Label")

    # Load an image for the button
    image = PhotoImage(file="C:\\Users\\Admin\\OneDrive\\Pictures\\Camera Roll\\download.png")

    # Create an image button
    image_button = tk.Button(root, image=image, command=update_label)
    image_button.pack(side=tk.TOP, padx=10, pady=10)

    # Create a dynamic text label
    label = tk.Label(root, text="")
    label.pack(side=tk.TOP, padx=10, pady=10)
    
    # Run the tkinter main loop
    root.mainloop()
