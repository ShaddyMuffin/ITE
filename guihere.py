def callit():
    import tkinter as tk
    from tkinter import PhotoImage
    import ttv
    import stt

    # Function to update the text in the label and call another function
    def update_text():
        new_text = stt.convt()  # Call a function to get new text
        label.config(text=new_text)  
        root.update() # Update the text in the label
        ttv.videoPlayer(new_text)

    # Create the main window
    root = tk.Tk()
    root.title("Speech to Text")

    # Load an image for the button
    button_image = PhotoImage(file="C:\\Users\\Admin\\OneDrive\\Pictures\\Camera Roll\\download.png")

    # Create an image button
    image_button = tk.Button(root, image=button_image, command=update_text) # command = function , the function is called when the button is clicked
    image_button.pack(side=tk.TOP, padx=10, pady=10)

    # Create a label with initial text
    label = tk.Label(root, text="", font=("Arial", 14))
    label.pack(side=tk.TOP,padx=10, pady=10)

    # Start the main loop
    print("Hit the button to Start the communication!".center(80))
    print()
    root.mainloop()
