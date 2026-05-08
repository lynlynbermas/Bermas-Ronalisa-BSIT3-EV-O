from tkinter import *

# Create window
root = Tk()
root.title("Tkinter Canvas Assignment")
root.geometry("500x500")

# Create canvas
canvas = Canvas(root, width=500, height=500, bg="white")
canvas.pack()

# Draw blue square
canvas.create_rectangle(50, 50, 200, 200, fill="blue")

# Draw green circle
canvas.create_oval(250, 50, 400, 200, fill="green")

# Add name below
canvas.create_text(250, 300, text="Ronalisa Bermas", font=("Arial", 20, "bold"))

# Run window
root.mainloop()