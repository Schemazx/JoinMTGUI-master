from tkinter import *
import webbrowser
import getpass
from tkinter import messagebox
from tkinter import Menu



class MainGUI(Tk):
    def createMain(self):
        self.menuGui = Menu(master=self)
        self.settings = Menu(self.menuGui, tearoff=0)
        self.settings.add_command(label="Credits", command=self.open_credits)
        self.settings.add_separator()
        self.settings.add_command(label="Quit", command=self.quit)
        self.menuGui.add_cascade(label="Menu", menu=self.settings)
        
        self.label = Label(self, text="Welcome "+getpass.getuser()+" to the JoinMT menu!\nRemember to put your class code in the blank")
        self.entry = Entry(self, bg="#BDBDBD")
        self.button = Button(self, text="Join", command=self.join_code, bd=5, cursor="hand2")
        self.label.pack(), self.entry.pack(), self.button.pack()
        
    def join_code(self):
        limit = len(self.entry.get())
        if (limit == 12):
            webbrowser.open("https://meet.google.com/"+self.entry.get())
        else:
            messagebox.showwarning("Invalid code", "The code must have 12 digits")
            
    def open_credits(self):
        credits = Toplevel()
        credits.title("Credits")
        label = Label(credits, text="Developer: Schema\n Discord: Schema#1036", font=("Arial Bold", 25))
        label.pack()          
            
    def __init__(self):
        Tk.__init__(self)
        self.createMain()
        self.config(menu=self.menuGui)
        
if __name__ == "__main__":
    client = MainGUI()
    client.title("JoinMT GUI")
    client.mainloop()
