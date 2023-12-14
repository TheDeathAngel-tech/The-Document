import mysql.connector, customtkinter, datetime as dt, time as time, requests
from mysql.connector import Error

customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")

app = customtkinter.CTk()
app.title("Das Dokument|Login")
app.geometry("600x500")
app.resizable(False, False)

app.label = customtkinter.CTkLabel(app, text="Login", font=("Arial", 20))
app.label.pack(pady=20)

app.textlabel = customtkinter.CTkLabel(app, text="Username", font=("Arial", 20))
app.textlabel.pack(pady=20)
app.input = customtkinter.CTkEntry(app, width=20)
app.input.pack(pady=20)

app.textlabel2 = customtkinter.CTkLabel(app, text="Password", font=("Arial", 20))
app.textlabel2.pack(pady=20)
app.input2 = customtkinter.CTkEntry(app, width=20)
app.input2.pack(pady=20)

app.mainloop