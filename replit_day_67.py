import tkinter as tk

window = tk.Tk()
window.title("Guess Who?") 
window.geometry("400x200") 

#change image based on user input
def changeImage():
    global newImage
    text_value = text.get("1.0", "end").strip().lower()

    if text_value == "Charlotte":
        newImage =tk.PhotoImage(file = "charlotte.png")
    elif text_value == "Gerald":
        newImage =tk.PhotoImage(file = "gerald.png")
    elif text_value == "Kate":
        newImage =tk.PhotoImage(file = "kate.png")
    elif text_value == "Mo":
        newImage =tk.PhotoImage(file = "mo.png")
    else: 
        hello["text"] = "Unable to find this user"
    
    canvas.itemconfig(container, image = newImage)

hello = tk.Label(text = "Guess Who? ") 
hello.pack() 

text = tk.Text(window ,height=1, width = 50)
text.pack()

button = tk.Button(text = "Let's Find Out!", command = changeImage) 
button.pack()

canvas = tk.Canvas(window, width = 300, height=150) # Creates a placeholder for the image in the window.
canvas.pack()

#user's photo
charlotte = tk.PhotoImage(file="charlotte.png")
gerald = tk.PhotoImage(file="gerald.png")
kate = tk.PhotoImage(file="kate.png")
mo = tk.PhotoImage(file="mo.png")

#start the guess from one user
container = canvas.create_image(150,1,image=mo) #creates image and sets the co-ordinates for it (150 is horizontal center).
######

tk.mainloop()