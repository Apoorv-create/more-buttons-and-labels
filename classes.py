from tkinter import *
 
root = Tk()
root.geometry("500x500")
root.title("Press a button to make a new button and label")

class CreateElements:
    
    def __init__(self):
        print("These are classes")
        
    def createNewElement(self):    
        label = Label(root, text = "Press this button to make more buttons and labels", fg="blue")
        label.pack() 
        btn = Button(root, text = "Press me", command = self.message)
        btn.pack(padx = 30, pady = 20)
        
    def message(self):
        messagebox.showinfo("showinfo", "You clicked me and now there are more buttons and labels")
        
obj_of_createElements = CreateElements()

btn = Button(root, text = "click me to make more of me and labels too", command = obj_of_createElements.createNewElement)
btn.pack(padx = 30, pady = 20)
root.mainloop()
    