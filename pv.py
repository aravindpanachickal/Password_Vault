#This is a program written in python3.
#Meant to be a Pass Word Manager
#Author : Aravind_Panachickal
#Project started on : 17-Feb-2022

#importing modules
import tkinter as tk
import sqlite3

#initialising GUI
root = tk.Tk()
#positioning the window on the screen
root.geometry('+850+1')
#adding title
root.title("Passowrd Vault")

#inserting icon to the window
photo = tk.PhotoImage(file = "icon.png")
root.iconphoto(True, photo)

#initialising sql
with sqlite3.connect('.pv_database.db') as db:
	cursor = db.cursor()

#checing and creating table for mpin
cursor.execute("""
CREATE TABLE IF NOT EXISTS Mpin(
id INTEGER PRIMARY KEY,
mpin TEXT NOT NULL,
recoverykey TEXT NOT NULL);
""")
#checing and creating table for vault
cursor.execute("""
CREATE TABLE IF NOT EXISTS vault(
id INTEGER PRIMARY KEY,
website TEXT NOT NULL,
username TEXT NOT NULL,
password TEXT NOT NULL);
""")

#GUI update
root.resizable(False, False)
root.mainloop()
