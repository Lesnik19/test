from tkinter import *
import customtkinter

customtkinter.set_appearance_mode("System")

customtkinter.set_default_color_there("blue")
app = customtkinter.CTk()
app.geometry("400x240")

def button_function():
    print('Кнопка нажата')

button = customtkinter.CTkButton(master=app, text='text', command=button_function)
button.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)
app.mainloop()
