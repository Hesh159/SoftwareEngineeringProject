import tkinter
from tkinter import *
import customtkinter
from PIL import Image, ImageTk

class TrafficGUI(customtkinter.CTk):
    APP_NAME = "Traffic Light System"
    WIDTH = 1300
    HEIGHT = 900

    def __init__(self):
        super().__init__()

        #Adding columns and rows to the GUI to be able to place things within it
        #self.grid_columnconfigure(1, weight=3)
        #self.grid_rowconfigure(1, weight=1)

        #Favicon, App name and sizing
        self.title(TrafficGUI.APP_NAME)
        self.iconbitmap('light.ico')
        self.geometry(f"{TrafficGUI.WIDTH}x{TrafficGUI.HEIGHT}")
        self.minsize(TrafficGUI.WIDTH, TrafficGUI.HEIGHT)
        self.maxsize(TrafficGUI.WIDTH, TrafficGUI.HEIGHT)
        self.resizable(False, False)

        #Sidebar
        self.frame_right = customtkinter.CTkFrame(master=self, width=450, height=self.HEIGHT, corner_radius=0, fg_color="#24272b")
        self.frame_right.place(relx=1, rely=0.5, anchor=tkinter.E)
        self.title1 = customtkinter.CTkLabel(master=self.frame_right, text="Pedestrian Crossing Button", text_font=("Roboto Medium", -26), text_color="white")
        self.title1.place(relx=0.5, rely=0.08, anchor=tkinter.CENTER)

        self.pedestrian_button = customtkinter.CTkButton(master=self.frame_right, text="Activate Light", corner_radius=6, width=200, command=self.button_event)
        self.pedestrian_button.place(relx=0.5, rely=0.13, anchor=tkinter.CENTER)

        self.pedestrian_button2 = customtkinter.CTkButton(master=self.frame_right, text="Deactivate Light", corner_radius=6, width=200, command=self.button_event2)
        self.pedestrian_button2.place(relx=0.5, rely=0.18, anchor=tkinter.CENTER)

        #Traffic lights
        self.light_color = "brown2"
        self.frame_left = customtkinter.CTkFrame(master=self, width=850, height=self.HEIGHT, corner_radius=0, fg_color="pink")
        self.frame_left.place(relx=0, rely=0.5, anchor=tkinter.W)
        self.canvas = tkinter.Canvas(self.frame_left, width=850, height=self.HEIGHT, highlightthickness=0)
        self.canvas.pack()
        self.image2 = Image.open('traffic3.png').resize((850, self.HEIGHT))
        self.bg_image2 = ImageTk.PhotoImage(self.image2)
        self.canvas.create_image(0, 0, anchor=NW, image=self.bg_image2)
        self.canvas.create_oval(415, 75, 430, 90, fill=self.light_color, width=0)

    def button_event(self):
        self.light_color = "SeaGreen2"
        self.canvas.create_oval(415, 75, 430, 90, fill=self.light_color, width=0) #redraw button
        print("button pressed")

    def button_event2(self):
        self.light_color = "brown2"
        self.canvas.create_oval(415, 75, 430, 90, fill=self.light_color, width=0) #redraw button
        print("button2 pressed")

if __name__ == "__main__":
    app = TrafficGUI()
    app.mainloop()


"""

Tom Schimansky's CustomTKinter UI-Library has been used for this program
Some CustomTKinter samples from his GitHub have been referenced
Reference Link: https://github.com/TomSchimansky

"""