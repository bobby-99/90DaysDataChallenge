import tkinter
from tkinter import messagebox, ttk

import openpyxl
from openpyxl import load_workbook

file_path = r"C:\Users\ichotu\Documents\90Days\resources\tkinter_practise.xlsx"
worksheet = openpyxl.load_workbook(file_path)
registration = worksheet["Registration"]

root = tkinter.Tk()
root.title("Student Registration Form")
root.geometry("500x250")
#root.configure(bg = "#404040")

def OnClickSubmit():
    name = name_box.get()
    email = email_box.get()
    phone = phone_box.get()
    branch = branch_dd.get()
    agree = agree_val.get()
    if name and email and phone and branch and agree == 1:
        messagebox.showinfo("Status", "Input Taken")
        registration.append([name, email, phone, branch, "YES"])
        worksheet.save(file_path)
    else:
        messagebox.showinfo("Warning", "Fill out all boxes")

# name
name_label = tkinter.Label(root, text="Name: ")
name_label.pack(anchor=tkinter.W, padx= 20)
name_box = tkinter.Entry(root)
name_box.pack(anchor=tkinter.W, padx= 20)

# Email
email_label = tkinter.Label(root, text="Email: ")
email_label.pack(anchor=tkinter.W, padx= 20)
email_box = tkinter.Entry(root)
email_box.pack(anchor=tkinter.W, padx= 20)

#phone entry
phone_label = tkinter.Label(root, text="Phone Number: ")
phone_label.pack(anchor=tkinter.W, padx= 20)
phone_box = tkinter.Entry(root)
phone_box.pack(anchor=tkinter.W, padx= 20)

# branch dropdown
choices = ["MECH", "CS", "ECE", "EEE"]
branch_label = tkinter.Label(root, text="Select Branch: ")
branch_label.pack(anchor=tkinter.W, padx= 20)
branch_dd = ttk.Combobox(root, values=choices)
branch_dd.pack(anchor=tkinter.W, padx= 20)

# terms checkbox
agree_val = tkinter.IntVar()
terms_check = ttk.Checkbutton(root, text="Do you agree to terms & conditions", variable=agree_val)
terms_check.pack(anchor=tkinter.W, padx=20, pady= 5)

# submit button
submit_button = tkinter.Button(root, text= "SUBMIT", command=OnClickSubmit)
submit_button.pack(anchor=tkinter.W, padx= 20)

root.mainloop()

