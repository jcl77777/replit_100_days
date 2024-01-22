import tkinter as tk
window = tk.Tk()
window.title("Black Mirror")
window.geometry("400x400")

#starting story
story = "You are in the era of AI robots. News said they are coming to take people's brains..."

#user given with two choices in each stage
def choice1():
    global story
    canvas.itemconfig(container, image = image2)
    story = "I want to hide away. They won't catch me. "
    storyLabel ["text"] = story
    #hide existing buttons and show next buttons
    button.pack_forget()
    button2.pack_forget()
    button3.pack()
    button4.pack()

def choice2():
    global story
    canvas.itemconfig(container, image = image3)
    story = "I am good friends with AI robots. It's nonsense. "
    storyLabel ["text"] = story
    #hide existing buttons and show next buttons
    button.pack_forget()
    button2.pack_forget()
    button5.pack()
    button6.pack()

#all choices 3, 4, 5, 6 leads to one sad ending and then restart
def choice3():
    global story
    canvas.itemconfig(container, image = image4)
    story = "The door is knocking...I need to call the police. "
    storyLabel ["text"] = story
    #hide existing buttons and show next buttons
    button3.pack_forget()
    button4.pack_forget()
    restart.pack()

def choice4():
    global story
    canvas.itemconfig(container, image = image4)
    story = "I am fully armed...Let's fight!"
    storyLabel ["text"] = story
    #hide existing buttons and show next buttons
    button3.pack_forget()
    button4.pack_forget()
    restart.pack()

def choice5():
    global story
    canvas.itemconfig(container, image = image4)
    story = "I should call my robot friend Amy. Where is her phone number? "
    storyLabel ["text"] = story
    #hide existing buttons and show next buttons
    button5.pack_forget()
    button6.pack_forget()
    restart.pack()

def choice6():
    global story
    canvas.itemconfig(container, image = image4)
    story = "I just met Dodi last week. He said he is visiting today. "
    storyLabel ["text"] = story
    #hide existing buttons and show next buttons
    button5.pack_forget()
    button6.pack_forget()
    restart.pack()

def restart():
    global story
    canvas.itemconfig(container, image = image1)
    story = "You are in the era of AI robots. News said they are coming to take people's brains..."
    storyLabel ["text"] = story
    #hide existing buttons and show next buttons
    restart.pack_forget()
    button.pack()
    button2.pack()

#images
image1 = tk.PhotoImage(file ="1.png")
image2 = tk.PhotoImage(file ="2.png")
image3 = tk.PhotoImage(file ="3.png")
image4 = tk.PhotoImage(file ="4.png")


canvas = tk.Canvas(window, width = 300, height = 200)
canvas.pack()
container = canvas.create_image(150,150, image = image1)

storyLabel = tk.Label(text = story)
storyLabel.pack()

#buttons
button = tk.Button(text = "1", command = choice1)
button2 = tk.Button(text = "2", command = choice2)
button3 = tk.Button(text = "3", command = choice3)
button4 = tk.Button(text = "4", command = choice4)
button5 = tk.Button(text = "5", command = choice5)
button6 = tk.Button(text = "6", command = choice6)
restart = tk.Button(text = "Restart", command = restart)

tk.mainloop()