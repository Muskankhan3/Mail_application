import smtplib
from tkinter import *


def send_message():
    address_info = address.get()
    email_body_info = email_body.get()
    sender_info = sender_address.get()
    password_info = password.get()
    subject_info = subject_info.get()
    
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(sender_info, password_info)

    print("Login successful")

    server.sendmail(sender_info, address_info,subject_info, email_body_info)
    print("Message sent")
    
    address_entry.delete(0, END)
    email_body_entry.delete(0, END)
    password_entry.delete(0, END)
    subject_entry.delete(0, END)
    sender_address_entry.delete(0, END)
    
    

gui = Tk()
gui.geometry("500x500")
gui.title("Email Sender App")
gui.configure(background="light grey")

heading = Label(text="Email Sender App", bg="white", fg="black", font="Helvetica 10 bold", width="500", height="3")
heading.pack()

sender_address_field = Label(text="From:     ")
sender_address_field.place(x=15, y=70)

sender_address = StringVar()
sender_address_entry = Entry(textvariable=sender_address, width="30")
sender_address_entry.place(x=15, y=100)

sender_password_field = Label(text="App Password:")
sender_password_field.place(x=15, y=140)

password = StringVar()
password_entry = Entry(textvariable=password, width="30", show="*")
password_entry.place(x=15, y=170)

address_field = Label(text="To:     ")
address_field.place(x=15, y=210)

address = StringVar()
address_entry = Entry(textvariable=address, width="30")
address_entry.place(x=15, y=240)

subject_field = Label(text="Subject:     ")
subject_field.place(x=15, y=280)

subject = StringVar()
subject_entry = Entry(textvariable=subject, width="30")
subject_entry.place(x=15, y=310)

email_body_field = Label(text="Message:")
email_body_field.place(x=15, y=350)

email_body = StringVar()
email_body_entry = Entry(textvariable=email_body, width="30")
email_body_entry.place(x=15, y=380, height="100")

button = Button(gui, text="Send Message", command=send_message, width="30", height="2", bg="light green")
button.place(x=15, y=500)

mainloop()
