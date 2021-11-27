from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
# Password Generator Project

def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_numbers + password_symbols + password_letters
    shuffle(password_list)

    password = ''.join(password_list)
    password_entry.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
# def entry_is_ok(*entries):
#     for entry in entries:
#         if entry == None:
#             return False

# def save(website, username, password):
#     '''Input parameters should be entry class.'''
#     new_website = website.get()
#     new_username = username.get()
#     new_password = password.get()
#     # is_ok = True
#     # if not entry_is_ok(new_website, new_username, new_password):
#     #     messagebox.showwarning(title='Oops', message="Please don't leave any fields empty!")
#     #     is_ok = False
#     # else:
#     #     is_ok = messagebox.askokcancel(title=new_website, message=f"These are the details entered: \nEmail: {new_username} "
#     #                                                       f"\n Password: {new_password} \nIs it ok to save?")
#     if len(new_website) == 0 or len(new_password) == 0:
#         messagebox.showwarning(title="Oops", message="Please make sure you haven't left any fields empty.")
#     else:
#         is_ok = messagebox.askokcancel(title=new_website, message=f"These are the details entered: \nEmail: {new_username} "
#                                                                   f"\n Password: {new_password} \nIs it ok to save?")
#         if is_ok:
#             with open('data.txt', 'a') as f:
#                 f.write(f"{new_website} | {new_username} | {new_password}\n")
#                 website.delete(0, END)
#                 password.delete(0, END)

def save():
    new_website = website_entry.get()
    new_username = username_entry.get()
    new_password = password_entry.get()
    if len(new_website) == 0 or len(new_password) == 0:
        messagebox.showwarning(title="Oops", message="Please make sure you haven't left any fields empty.")
    else:
        is_ok = messagebox.askokcancel(title=new_website,
                                       message=f"These are the details entered: \nEmail: {new_username} "
                                               f"\n Password: {new_password} \nIs it ok to save?")
        if is_ok:
            with open('data.txt', 'a') as f:
                f.write(f"{new_website} | {new_username} | {new_password}\n")
                website_entry.delete(0, END)
                password_entry.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title('Password Manager')
window.config(padx=20, pady=20)

canvas = Canvas(width=200, height=200, highlightthickness=0)
logo = PhotoImage(file='logo.png')
canvas.create_image(100, 100, image=logo)
canvas.grid(column=1, row=0)

# Labels
website_label = Label(text='Website:')
website_label.grid(column=0, row=1)
username_label = Label(text='Email/Username:')
username_label.grid(column=0, row=2)
password_label = Label(text='Password:')
password_label.grid(column=0, row=3)

# Entries
website_entry = Entry(width=52)
website_entry.grid(column=1, row=1, columnspan=2)
website_entry.focus()
username_entry = Entry(width=52)
username_entry.insert(0, 'anasnurf99@gmail.com')
username_entry.grid(column=1, row=2, columnspan=2)
password_entry = Entry(width=33)
password_entry.grid(column=1, row=3)

# Buttons
generate_pw = Button(text='Generate Password', command=generate_password)
generate_pw.grid(column=2, row=3)
# add_pw = Button(text='Add', width=45, command=lambda: save(website_entry, username_entry, password_entry))
add_pw = Button(text='Add', width=45, command=save)
add_pw.grid(column=1, row=4, columnspan=2)

window.mainloop()
