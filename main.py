import mysql.connector, customtkinter, datetime as dt, time as time, requests
from mysql.connector import Error

customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")

app = customtkinter.CTk()
app.geometry("600x500")
app.resizable(False, False)
app.title("Das Dokument | Login")

# MySQL Connection
try:
    connection = mysql.connector.connect(host="62.171.164.75", database="DasDokument", user="system", password="BZwpCdIKsKM4MREYV8Bi")
    if connection.is_connected():
        db_Info = connection.get_server_info()
        print("Connected to MySQL Server version ", db_Info)
        cursor = connection.cursor()
except Error as e:
    print("Error while connecting to MySQL", e)

app.mainloop()