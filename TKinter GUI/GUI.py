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

        #Favicon, App name and sizing
        self.title(TrafficGUI.APP_NAME)
        self.iconbitmap('light.ico')
        self.geometry(f"{TrafficGUI.WIDTH}x{TrafficGUI.HEIGHT}")
        self.minsize(TrafficGUI.WIDTH, TrafficGUI.HEIGHT)
        self.maxsize(TrafficGUI.WIDTH, TrafficGUI.HEIGHT)
        self.resizable(False, False)

        #Variables from other classes
        self.t1number = 0;

        #Sidebar
        self.frame_right = customtkinter.CTkFrame(master=self, width=450, height=self.HEIGHT, corner_radius=0, fg_color="#24272b")
        self.frame_right.place(relx=1, rely=0.5, anchor=tkinter.E)
        self.title1 = customtkinter.CTkLabel(master=self.frame_right, text="Traffic Light System", text_font=("Roboto Medium", -26), text_color="white")
        self.title1.place(relx=0.5, rely=0.08, anchor=tkinter.CENTER)

        self.button_container = customtkinter.CTkFrame(master=self.frame_right, width=400, height=170, corner_radius=8, fg_color="#17181a")
        self.button_container.place(relx=0.5, rely=0.22, anchor=tkinter.CENTER)

        #Sidebar buttons
        self.title2 = customtkinter.CTkLabel(master=self.button_container, text="Pedestrian Button", text_font=("Roboto Medium", -20), text_color="white")
        self.title2.place(relx=0.5, rely=0.15, anchor=tkinter.CENTER)
        self.pedestrian_button = customtkinter.CTkButton(master=self.button_container, text="Light One", corner_radius=6, width=200, 
                                                        height=35, command=self.button_event, text_font=("Roboto Medium", -17), fg_color="steel blue")
        self.pedestrian_button.place(relx=0.5, rely=0.42, anchor=tkinter.CENTER)

        self.pedestrian_button2 = customtkinter.CTkButton(master=self.button_container, text="Light Two", corner_radius=6, width=200, 
                                                        height=35, command=self.button_event2, text_font=("Roboto Medium", -17), fg_color="steel blue")
        self.pedestrian_button2.place(relx=0.5, rely=0.74, anchor=tkinter.CENTER)

        #Sidebar statistics
        self.title3 = customtkinter.CTkLabel(master=self.frame_right, text="Traffic Count", text_font=("Roboto Medium", -21), text_color="white")
        self.title3.place(relx=0.5, rely=0.385, anchor=tkinter.CENTER)
        self.text1 = customtkinter.CTkLabel(master=self.frame_right, text="Light 1: X", text_font=("Ariel", -17), text_color="white")
        self.text1.place(relx=0.35, rely=0.44, anchor=tkinter.W)
        self.text2 = customtkinter.CTkLabel(master=self.frame_right, text="Light 2: X", text_font=("Ariel", -17), text_color="white")
        self.text2.place(relx=0.35, rely=0.48, anchor=tkinter.W)
        self.text3 = customtkinter.CTkLabel(master=self.frame_right, text="Light 3: X", text_font=("Ariel", -17), text_color="white")
        self.text3.place(relx=0.35, rely=0.52, anchor=tkinter.W)
        self.text4 = customtkinter.CTkLabel(master=self.frame_right, text="Light 4: X", text_font=("Ariel", -17), text_color="white")
        self.text4.place(relx=0.35, rely=0.56, anchor=tkinter.W)
        self.text5 = customtkinter.CTkLabel(master=self.frame_right, text="Light 5: X", text_font=("Ariel", -17), text_color="white")
        self.text5.place(relx=0.35, rely=0.6, anchor=tkinter.W)
        self.text6 = customtkinter.CTkLabel(master=self.frame_right, text="Light 6: X", text_font=("Ariel", -17), text_color="white")
        self.text6.place(relx=0.35, rely=0.64, anchor=tkinter.W)
        self.text7 = customtkinter.CTkLabel(master=self.frame_right, text="Light 7: X", text_font=("Ariel", -17), text_color="white")
        self.text7.place(relx=0.35, rely=0.68, anchor=tkinter.W)
        self.text8 = customtkinter.CTkLabel(master=self.frame_right, text="Light 8: X", text_font=("Ariel", -17), text_color="white")
        self.text8.place(relx=0.35, rely=0.72, anchor=tkinter.W)

        self.title4 = customtkinter.CTkLabel(master=self.frame_right, text="Total Traffic", text_font=("Roboto Medium", -21), text_color="white")
        self.title4.place(relx=0.5, rely=0.8, anchor=tkinter.CENTER)
        self.text8 = customtkinter.CTkLabel(master=self.frame_right, text="Total: XX", text_font=("Ariel", -17), text_color="white")
        self.text8.place(relx=0.35, rely=0.855, anchor=tkinter.W)

        #Traffic lights
        self.frame_left = customtkinter.CTkFrame(master=self, width=850, height=self.HEIGHT, corner_radius=0, fg_color="pink")
        self.frame_left.place(relx=0, rely=0.5, anchor=tkinter.W)
        self.canvas = tkinter.Canvas(self.frame_left, width=850, height=self.HEIGHT, highlightthickness=0)
        self.canvas.pack()
        self.image2 = Image.open('traffic3.png').resize((850, self.HEIGHT))
        self.bg_image2 = ImageTk.PhotoImage(self.image2)
        self.canvas.create_image(0, 0, anchor=NW, image=self.bg_image2)

        #Pedestrian light 1
        self.canvas.create_oval(415, 75, 430, 90, fill="brown2", width=0)
        #Pedestrian light 2
        self.canvas.create_oval(415, 665, 430, 680, fill="brown2", width=0)

        #Traffic light 1
        self.canvas.create_oval(340, 75, 355, 90, fill="SeaGreen2", width=0)
        self.canvas.create_oval(360, 75, 375, 90, fill="SeaGreen2", width=0)
        #Traffic light 2
        self.canvas.create_oval(630, 75, 645, 90, fill="SeaGreen2", width=0)
        self.canvas.create_oval(650, 75, 665, 90, fill="SeaGreen2", width=0)
        #Traffic light 3
        self.canvas.create_oval(480, 195, 495, 210, fill="SeaGreen2", width=0)
        #Traffic light 4
        self.canvas.create_oval(560, 195, 575, 210, fill="SeaGreen2", width=0)
        self.canvas.create_oval(580, 195, 595, 210, fill="SeaGreen2", width=0)
        #Traffic light 5
        self.canvas.create_oval(240, 665, 255, 680, fill="SeaGreen2", width=0)
        self.canvas.create_oval(260, 665, 275, 680, fill="SeaGreen2", width=0)
        #Traffic light 6
        self.canvas.create_oval(350, 665, 365, 680, fill="SeaGreen2", width=0)
        #Traffic light 7
        self.canvas.create_oval(95, 785, 110, 800, fill="SeaGreen2", width=0)
        self.canvas.create_oval(115, 785, 130, 800, fill="SeaGreen2", width=0)
        #Traffic light 8
        self.canvas.create_oval(470, 785, 485, 800, fill="SeaGreen2", width=0)
        self.canvas.create_oval(490, 785, 505, 800, fill="SeaGreen2", width=0)


    #Buttons
    def button_event(self):
        self.after(1000, self.redrawLight1, "brown2")
        self.after(1000, self.redrawLight3, "brown2")
        self.after(4000, self.redrawPLight1, "SeaGreen2")
        self.after(9000, self.redrawPLight1, "brown2")
        self.after(11000, self.redrawLight1, "SeaGreen2")
        self.after(11000, self.redrawLight3, "SeaGreen2")


    def button_event2(self):
        self.after(1000, self.redrawLight6, "brown2")
        self.after(1000, self.redrawLight8, "brown2")
        self.after(4000, self.redrawPLight2, "SeaGreen2")
        self.after(9000, self.redrawPLight2, "brown2")
        self.after(11000, self.redrawLight6, "SeaGreen2")
        self.after(11000, self.redrawLight8, "SeaGreen2")

    #Traffic light color redraw

        #PEDESTRIAN
    def redrawPLight1(self, color): #PEDESTRIAN 1
        self.canvas.create_oval(415, 75, 430, 90, fill=color, width=0) #redraw light

    def redrawPLight2(self, color): #PEDESTRIAN 2
        self.canvas.create_oval(415, 665, 430, 680, fill=color, width=0) #redraw light

        #REGULAR TRAFFIC LIGHT
    def redrawLight1(self, color): #TRAFFIC 1
        self.canvas.create_oval(340, 75, 355, 90, fill=color, width=0)
        self.canvas.create_oval(360, 75, 375, 90, fill=color, width=0) #redraw light

    def redrawLight2(self, color): #TRAFFIC 2
        self.canvas.create_oval(630, 75, 645, 90, fill=color, width=0)
        self.canvas.create_oval(650, 75, 665, 90, fill=color, width=0) #redraw light

    def redrawLight3(self, color): #TRAFFIC 3
        self.canvas.create_oval(480, 195, 495, 210, fill=color, width=0) #redraw light

    def redrawLight4(self, color): #TRAFFIC 4
        self.canvas.create_oval(560, 195, 575, 210, fill=color, width=0)
        self.canvas.create_oval(580, 195, 595, 210, fill=color, width=0) #redraw light
    
    def redrawLight5(self, color): #TRAFFIC 5
        self.canvas.create_oval(240, 665, 255, 680, fill=color, width=0)
        self.canvas.create_oval(260, 665, 275, 680, fill=color, width=0) #redraw light

    def redrawLight6(self, color): #TRAFFIC 6
        self.canvas.create_oval(350, 665, 365, 680, fill=color, width=0) #redraw light
    
    def redrawLight7(self, color): #TRAFFIC 7
        self.canvas.create_oval(95, 785, 110, 800, fill=color, width=0)
        self.canvas.create_oval(115, 785, 130, 800, fill=color, width=0) #redraw light

    def redrawLight8(self, color): #TRAFFIC 8
        self.canvas.create_oval(470, 785, 485, 800, fill=color, width=0)
        self.canvas.create_oval(490, 785, 505, 800, fill=color, width=0) #redraw light
    

    #Traffic
    '''TO DO'''

if __name__ == "__main__":
    app = TrafficGUI()
    app.mainloop()


"""

Tom Schimansky's CustomTKinter UI-Library has been used for this program
Some CustomTKinter samples from his GitHub have been referenced
Reference Link: https://github.com/TomSchimansky

"""