import mysql.connector, customtkinter, datetime as dt, time as time, requests
from mysql.connector import Error

app = customtkinter.CTk()	
app.title("Das Dokument|Login")
app.geometry("600x500")
app.resizable(False, False)

app.mainloop