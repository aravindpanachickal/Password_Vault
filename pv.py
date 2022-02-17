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

#clearing the widgets
def screen_clear():
	for widget in root.winfo_children():
		widget.destroy()

#vault_gui
def vault():
	screen_clear()
	direction = "Enter Master Pin"
	direction_1 = tk.Label(font=("courier"), text=direction)
	direction_1.grid(column=0, row=0)

	masterPin = tk.Entry(justify="center")
	masterPin.grid(column=0, row=1)

	confirmButton_1 = tk.Button(font=('courier'), text='Confirm Pin', command=lambda:condition_check(masterPin.get()))
	confirmButton_1.grid(column=0, row=2)

	btn0 = tk.Button(font=('courier'), text=0, command=lambda:masterPin.insert(len(masterPin.get()), 0))
	btn0.grid(column=1, row=1)
	btn1 = tk.Button(font=('courier'), text=1, command=lambda:masterPin.insert(len(masterPin.get()), 1))
	btn1.grid(column=2, row=1)
	btn2 = tk.Button(font=('courier'), text=2, command=lambda:masterPin.insert(len(masterPin.get()), 2))
	btn2.grid(column=3, row=1)
	btn3 = tk.Button(font=('courier'), text=3, command=lambda:masterPin.insert(len(masterPin.get()), 3))
	btn3.grid(column=1, row=2)
	btn4 = tk.Button(font=('courier'), text=4, command=lambda:masterPin.insert(len(masterPin.get()), 4))
	btn4.grid(column=2, row=2)
	btn5 = tk.Button(font=('courier'), text=5, command=lambda:masterPin.insert(len(masterPin.get()), 5))
	btn5.grid(column=3, row=2)
	btn6 = tk.Button(font=('courier'), text=6, command=lambda:masterPin.insert(len(masterPin.get()), 6))
	btn6.grid(column=1, row=3)
	btn7 = tk.Button(font=('courier'), text=7, command=lambda:masterPin.insert(len(masterPin.get()), 7))
	btn7.grid(column=2, row=3)
	btn8 = tk.Button(font=('courier'), text=8, command=lambda:masterPin.insert(len(masterPin.get()), 8))
	btn8.grid(column=3, row=3)
	btn9 = tk.Button(font=('courier'), text=9, command=lambda:masterPin.insert(len(masterPin.get()), 9))
	btn9.grid(column=1, row=4)
	rstBtn = tk.Button(font=('courier'), text="Reset", command=lambda:masterPin.delete(0, len(masterPin.get())))
	rstBtn.grid(column=2, row=4, columnspan=2)
	directions_2 = tk.Label(font=('courier'), text="")
	directions_2.grid(column=0, row=4)

	def condition_check(mpin):
		print("authentic")


vault()
#GUI update
root.resizable(False, False)
root.mainloop()
