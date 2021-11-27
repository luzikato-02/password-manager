from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
import json


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
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
def save():
    website = website_entry.get()
    email = username_entry.get()
    password = password_entry.get()
    new_data = {
        website: {
            "email": email,
            "password": password,
        }
    }
    if len(website) == 0 or len(password) == 0:
        messagebox.showwarning(title="Oops", message="Please make sure you haven't left any fields empty.")
    else:
        try:
            # Try reading 'data.json'
            with open('data.json', 'r') as data_file:
                # Reading old data
                data = json.load(data_file)
        except FileNotFoundError:
            # File not found so create new file and put 'new_data' directly into that newly created file.
            with open('data.json', 'w') as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            # If 'try' section successful then update 'data' with 'new_data'
            data.update(new_data)
            # Append updated data to existing file
            with open('data.json', 'w') as data_file:
                json.dump(data, data_file, indent=4)
        finally:
            # Whatever happened clear entry
            website_entry.delete(0, END)
            password_entry.delete(0, END)
# ---------------------------- SEARCH WEBSITE ------------------------------- #
def find_password():
    website = website_entry.get()
    try:
        # Try opening 'data.json'
        with open('data.json', 'r') as data_file:
            # Reading old data
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showerror(title="Error", message="No data file found.")
    else:
        if website in data:
            email_data = data[website]["email"]
            password_data = data[website]["password"]
            messagebox.showinfo(title="Data Found",message=f"These are the data for {website} website: \nEmail: {email_data}"
                                                           f"\nPassword: {password_data}")
        else:
            messagebox.showerror(title="Error", message=f"Not details for {website} exists.")
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
website_entry = Entry(width=33)
website_entry.grid(column=1, row=1)
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
search = Button(text='Search', width=15, command=find_password)
search.grid(column=2, row=1)

window.mainloop()
