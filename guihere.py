def callit():
    import tkinter as tk
    from tkinter import PhotoImage
    import ttv

    # Function to update the text in the label and call another function
    def update_text():
        new_text = get_new_text()  # Call a function to get new text
        label.config(text=new_text)  # Update the text in the label
        root.update()
        after_update_function(new_text)  # Call another function after updating the text

    # Function to get new text (replace this with your logic to generate new text)
    def get_new_text():
        return ttv.run_model()

    # Function to be called after updating the text (replace this with your desired function)
    def after_update_function(n):
        ttv.videoPlayer(n)


    # Create the main window
    root = tk.Tk()
    root.title("Dynamic Text Label")

    # Load an image for the button
    button_image = PhotoImage(file="C:\\Users\\Admin\\OneDrive\\Pictures\\Camera Roll\\download.png")

    # Create an image button
    image_button = tk.Button(root, image=button_image, command=update_text)
    image_button.pack(side=tk.TOP, padx=10, pady=10)

    # Create a label with initial text
    label = tk.Label(root, text="", font=("Arial", 14))
    label.pack(side=tk.TOP,padx=10, pady=10)

    # Start the main loop
    root.mainloop()
