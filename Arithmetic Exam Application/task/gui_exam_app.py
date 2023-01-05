import tkinter
import customtkinter


customtkinter.set_appearance_mode("System")  # Modes: system (default), light, dark
customtkinter.set_default_color_theme("blue")  # Themes: blue (default), dark-blue, green
welcome_page = customtkinter.CTk()  # create CTk window like you do with the Tk window
welcome_page.geometry("1920x1080")
title = customtkinter.CTkLabel(master=welcome_page, text="Arithmetic Exam", font=('Bahnschrift SemiLight Condensed',40))
title.place(relx=0.5, rely=0.1, anchor=tkinter.N)

def button_function():

    q2 = customtkinter.CTkLabel(master=welcome_page, text="Enter Name:", font=('Bahnschrift SemiLight Condensed', 35))
    q2.place(relx=0.45, rely=0.3, anchor=tkinter.CENTER)
    entered = tkinter.StringVar(value='')
    name = customtkinter.CTkEntry(master=welcome_page, textvariable=entered, placeholder_text="Name")
    name.place(relx=0.51, rely=0.288)
    if entered.get() != "":
        name_entered()


def name_entered():
    q1 = customtkinter.CTkLabel(master=welcome_page, text="Which level?", font=('Bahnschrift SemiLight Condensed', 35))
    q1.place(relx=0.5, rely=0.3, anchor=tkinter.CENTER)
    level1_button = customtkinter.CTkButton(master=welcome_page, width=50, height=50,
                                            fg_color=('medium purple', 'medium purple'),
                                            hover_color=("dark orchid", "dark orchid"), text="1",
                                            font=('Bahnschrift SemiLight Condensed', 28))
    level1_button.place(relx=0.375, rely=0.425, anchor=tkinter.S)
    level2_button = customtkinter.CTkButton(master=welcome_page, width=50, height=50,
                                            fg_color=('medium purple', 'medium purple'),
                                            hover_color=("dark orchid", "dark orchid"), text="2",
                                            font=('Bahnschrift SemiLight Condensed', 28))
    level2_button.place(relx=0.525, rely=0.425, anchor=tkinter.S)
    description1 = customtkinter.CTkLabel(master=welcome_page, text="Simple operations\nwith numbers 2-9",
                                          font=('Bahnschrift SemiLight Condensed', 20))
    description1.place(relx=0.45, rely=0.425, anchor=tkinter.S)
    description2 = customtkinter.CTkLabel(master=welcome_page, text="Integral squares\nof 1-12",
                                          font=('Bahnschrift SemiLight Condensed', 20))
    description2.place(relx=0.59, rely=0.425, anchor=tkinter.S)

# Use CTkButton instead of tkinter Button
button = customtkinter.CTkButton(master=welcome_page, width=175, height=50, fg_color=('medium sea green', 'sea green'),
                                 hover_color=('sea green', 'medium sea green'), text="START",
                                 font=('Bahnschrift SemiLight Condensed', 28), command=button_function)
button.place(relx=0.5, rely=0.2, anchor=tkinter.CENTER)

welcome_page.mainloop()
